from typing import Any, Dict, List, Set, Tuple, Type, TypeVar, overload

##############################################################################
# 						CONSTANTS
##############################################################################
DEBUGGING_MODE = False


##############################################################################
# 						SYSTEM
##############################################################################


class System():
	def update(self, world:"World") -> None:
		raise Exception("ERROR: Class `{}` has NOT implemented its update() method".format(type(self).__name__))
	def __str__(self):
		return str(type(self)).split(".")[1].split("'")[0]+str(vars(self))
	def __repr__(self):
		return str(type(self)).split(".")[1].split("'")[0]+str(vars(self))


##############################################################################
# 						COMPONENT
##############################################################################

class Component():
	def pp(self):
		for attr in dir(self):
			if len(attr.split("__")) == 1:
				print("obj.%s = %r" % (attr, getattr(self, attr)))
	def __str__(self):
		return str(type(self)).split(".")[1].split("'")[0]+str(vars(self))
	def __repr__(self):
		return str(type(self)).split(".")[1].split("'")[0]+str(vars(self))


##############################################################################
# 						WORLD
##############################################################################

T = TypeVar("T")
T1 = TypeVar("T1", bound=Component)
T2 = TypeVar("T2", bound=Component)
T3 = TypeVar("T3", bound=Component)
T4 = TypeVar("T4", bound=Component)
T5 = TypeVar("T5", bound=Component)
T6 = TypeVar("T6", bound=Component)
T7 = TypeVar("T7", bound=Component)
T8 = TypeVar("T8", bound=Component)
T9 = TypeVar("T9", bound=Component)
T10 = TypeVar("T10", bound=Component)

##############################################################################
# 						WORLD
##############################################################################

""" 
Note: World can be further optimized for performance. Currently it is being optimized to clearly showcase how to implement ECS 
"""
class World():
	def __init__(self,*systems:System) -> None:
		
		self.entity_counter : int = 0
		self.systems : Tuple[System,...] = systems
		self.entity_to_component_dict : Dict[int,Dict[Type[Component],List[Component]]] = {} # Note that entities can have multiple of the SAME component. Note we are using List[Component] not Set[Component] or Tuple[Component], as tuple is constant and set does NOT preserve order component was added
		self.component_constructor_to_entities : Dict[Type[Component],Set[int]] = {}

		self.staged_removal_components_to_entity : Dict[Component,int] = {}

	# #########################################################
	# 					ENTITIES
	# #########################################################
	def add_entity(self,*components:Component) -> int:

		# 0.0 Check that there are no duplicate component instances
		if not len(set(components)) == len(components):
			raise Exception("ERROR: len(set(components)) == len(components)! You can NOT pass in the same component instance multiple times!")
		if len(components) == 0:
			raise Exception("ERROR: len(components) == 0! You can NOT create an entity with 0 components")
			print("WARNING: You did not add any components when calling <World>.add_entity()")


		# 1.0 Id
		# 1.1 Assign Id
		entity_id = self.entity_counter
		self.entity_counter+=1

		# 1.1 Sanity check - check if entity already exists
		if entity_id in self.entity_to_component_dict:
			raise Exception(f"ERROR: an entity with id of `{entity_id}` already exists!")


		# 2.0 Add entity and components to `entity_to_component_dict`
		# 2.1 Create dict as entity is new
		self.entity_to_component_dict[entity_id] = {}

		# 2.2 Create a dict that maps component constructors to components
		for component in components:
			component_constructor = type(component)

			# If new component_constructor added, create a new list to store components
			if not component_constructor in self.entity_to_component_dict[entity_id]:
				self.entity_to_component_dict[entity_id][component_constructor] = []
			self.entity_to_component_dict[entity_id][component_constructor].append(component)


		# 3.0 Add entity to `component_constructor_to_entities`
		for component in components:
			component_constructor = type(component)

			# If entity has new component_constructor, create a new set to store entities
			if not component_constructor in self.component_constructor_to_entities:
				self.component_constructor_to_entities[component_constructor] = set()
			self.component_constructor_to_entities[component_constructor].add(entity_id)

		return entity_id

	def remove_entities(self,*entities:int) -> None:
		""" 
			Question how much should I clean???
			 - Should I delete the sets if they don't have any entities in them?  eg: self.component_constructor_to_entities[component_constructor]
			 - Should I delete the arrays if they don't have any components in them? eg: self.entity_to_component_dict[entity][component_constructor]
			
			MY CHOICE: 
			- No, don't remove them. This way garbage collector does less work at the expense of a tiny memory overhead
		"""
		pass
		

		# 0.0 Check entity even exists
		# if 
		for entity in entities:
			if not entity in self.entity_to_component_dict:
				raise Exception(f"ERROR: {entity} does NOT exist. Perhaps it was already been deleted? Or mistake?")

		# 1.0 Remove entities from `component_constructor_to_entities`
		# 1.1 Iterate over all entities to collect their components' constructors
		for entity in entities:
			
			# For each of the component_constructors the entity has, remove this entity from `component_constructor_to_entities`
			for component_constructor in self.entity_to_component_dict[entity]:
				entity_set = self.component_constructor_to_entities[component_constructor]
				entity_set.discard(entity)


		# 2.0 Rememove entities from `entity_to_component_dict`
		for entity in entities:
			self.entity_to_component_dict.pop(entity)

	# #########################################################
	# 					COMPONENTS - ADD/DELETE
	# #########################################################
	def add_component_instances_to_entity(self,entity:int,*components:Component) -> None:
		# Adds component(s) from entity
		""" 
		Note: You can add multiple of the same type of component to the same entity. But you can't add the same component instance to the entity multiple times  
		"""

		# 0.0 Check entity exists
		if not entity in self.entity_to_component_dict:
			raise Exception(f"ERROR: {entity} does NOT exist in self.entity_to_component_dict!")
		
		# 0.1 Check that there are no duplicate component instances
		if not len(set(components)) == len(components):
			raise Exception("ERROR: len(set(components)) == len(components)! You can NOT pass in the same component instance multiple times!")
		

		# 1.0 Update self.component_constructor_to_entities
		# 1.1 Iterate over all components
		for component in components:
			component_constructor = type(component)

			# If component_constructor is new, create new set to store entities
			if not component_constructor in self.component_constructor_to_entities:
				self.component_constructor_to_entities[component_constructor] = set()
			self.component_constructor_to_entities[component_constructor].add(entity)


		# 2.0 Update self.entity_to_component_dict - map entities to Dict[component_constructor,component]
		for component in components:
			component_dict = self.entity_to_component_dict[entity]
			component_constructor = type(component)

			# If component constructor is new to component_dict, create new list to store components
			if not component_constructor in component_dict:
				component_dict[component_constructor] = []
			component_dict[component_constructor].append(component)



	def stage_remove_component_instances_from_entity(self,entity:int,*components:Component) -> None:
		# Removes component(s) from entity
		""" 
		Note: Remember that you can have multiple components of the same type. 
		"""
		
		# 0.0 Check entity exists
		if not entity in self.entity_to_component_dict:
			raise Exception("ERROR: `entity` does not exist in `self.entity_to_component_dict`!")
		
		# 0.05 Check for no duplicates
		if not len(components) == len(set(components)):
			raise Exception("ERROR: You can NOT specify the same component multiple times!")

		# 0.1 Check components actually exist on entity
		for component in components:
			component_constructor = type(component)


			if not component_constructor in self.entity_to_component_dict[entity]:
				raise Exception("ERROR: parameter/component constructor supplied does NOT exist on this entity!")
			if not component in self.entity_to_component_dict[entity][component_constructor]:
				raise Exception("ERROR: parameter/component of `remove_components_from_entity` must be an instance already assigned to the entity! Do not instantiate another component then pass it through as an argument!")
		
		# 1.0 Add component into staged
		for component in components:
			self.staged_removal_components_to_entity[component] = entity
			#  = self.staged_removal_components.union(components)

	def stage_remove_components_by_component_constructors_from_entity(self,entity:int,*component_constructors:Type[Component]) -> None:
		# 0.0 check if entity exists
		if not entity in self.entity_to_component_dict:
			raise Exception(f"ERROR: entity `{entity}` does NOT exist!")
		
		# 0.05 Check for no duplicates
		if not len(component_constructors) == len(set(component_constructors)):
			raise Exception("ERROR: You can NOT specify the same component_constructors multiple times!")
		
		# 0.1 Iterate over all component_constructors and check
		for component_constructor in component_constructors:
			if not component_constructor in self.entity_to_component_dict[entity]:
				raise Exception(f"ERROR: component_constructor {component_constructor} does not exist in self.entity_to_component_dict[entity]!")
			if len(self.entity_to_component_dict[entity][component_constructor]) == 0:
				raise Exception(f"ERROR: component_constructor `{component_constructor}` list on entity `{entity}` is 0!")
		

		# 1.0 Add relevant components into local set
		# 1.1 Collect all instances of component_constructors from entity
		local_staged_removal_components:List[Component] = []
		for component_constructor in component_constructors:
			local_staged_removal_components.extend(self.entity_to_component_dict[entity][component_constructor])   #.add(*)
			
		# 2.0 Update staged
		for component in local_staged_removal_components:
			self.staged_removal_components_to_entity[component] = entity

	def stage_remove_components_by_component_constructors_from_all_entities(self,*component_constructors:Type[Component]) -> None:
		# 0.0 Check component_constructors if exists
		for component_constructor in component_constructors:
			if not component_constructor in self.component_constructor_to_entities:
				raise Exception(f"ERROR: component_constructor `{component_constructor}` NOT in component_constructor_to_entities!")
				# Note, but there might not be any entities, just an empty list....
			if len(self.component_constructor_to_entities[component_constructor]) == 0:
				raise Exception(f"ERROR: `{component_constructor}` len(self.component_constructor_to_entities[component_constructor]) == 0")
			
		# 0.05 Check for no duplicates
		if not len(component_constructors) == len(set(component_constructors)):
			raise Exception("ERROR: You can NOT specify the same component_constructors multiple times!")

		# 1.0 Collect all component instances into a set
		for component_constructor in component_constructors:
			# 1.1 Get entities with component_constructors
			entity_set = self.component_constructor_to_entities[component_constructor]

			# 1.2 Using entities, find the actual component instances using component_constructor
			for entity in entity_set:
				component_list = self.entity_to_component_dict[entity][component_constructor]
				for component in component_list:
					# 2.0 Update staged 
					self.staged_removal_components_to_entity[component] = entity



	def remove_component_instances_from_entity(self,entity:int,*components:Component) -> None:
		# Removes component(s) from entity
		""" 
		Note: Remember that you can have multiple components of the same type. 
		"""
		
		# 0.0 Check entity exists
		if not entity in self.entity_to_component_dict:
			raise Exception("ERROR: `entity` does not exist in `self.entity_to_component_dict`!")
		
		# 0.1 Check components actually exist on entity
		for component in components:
			component_constructor = type(component)


			if not component_constructor in self.entity_to_component_dict[entity]:
				raise Exception("ERROR: parameter/component constructor supplied does NOT exist on this entity!")
			if not component in self.entity_to_component_dict[entity][component_constructor]:
				raise Exception("ERROR: parameter/component of `remove_components_from_entity` must be an instance already assigned to the entity! Do not instantiate another component then pass it through as an argument!")
		

		# 1.0 remove components from self.component_constructor_to_entities
		# If number of components of a certain type that exists in the entity > number of that certain type being passed in, then 'dont remove entity' else 'remove entity'
		# 1.1 Generate a frequency dict for each component_constructor
		component_constructor_to_frequency:Dict[Type[Component],int] = {}
		for component in components:
			component_constructor = type(component)

			# If component_constructor is first, create initial value
			if not component_constructor in component_constructor_to_frequency:
				component_constructor_to_frequency[component_constructor] = 0
			component_constructor_to_frequency[component_constructor] += 1	
		
		# 1.2 Compare frequency dict to actual frequency of entity. If frequency dict is = to actual frequency then delete
		for  component_constructor, frequency in component_constructor_to_frequency.items():
			actual_length = len(self.entity_to_component_dict[entity][component_constructor])

			if frequency == actual_length:
				# Remove entity
				self.component_constructor_to_entities[component_constructor].remove(entity)
			elif frequency > actual_length:
				# Sanity check
				raise Exception("ERROR: Your frequency should NEVER be above that of the actual. We have a bug!")


		# 2.0 remove components from self.entity_to_component_dict
		for component in components:
			component_constructor = type(component)

			component_list = self.entity_to_component_dict[entity][component_constructor]
			component_list.remove(component)

	def remove_components_by_component_constructors_from_entity(self,entity:int,*component_constructors:Type[Component]) -> None:
		# 0.0 check if entity exists
		if not entity in self.entity_to_component_dict:
			raise Exception(f"ERROR: entity `{entity}` does NOT exist!")
		
		# 1.0 Iterate over all component_constructors
		for component_constructor in component_constructors:
			# 1.1 Remove all instances of component_constructors from entity in self.entity_to_component_constructor_dict
			if not component_constructor in self.entity_to_component_dict[entity]:
				raise Exception(f"ERROR: component_constructor {component_constructor} does not exist in self.entity_to_component_dict[entity]!")
			if len(self.entity_to_component_dict[entity][component_constructor]) == 0:
				raise Exception(f"ERROR: component_constructor `{component_constructor}` list is 0!")
			self.entity_to_component_dict[entity][component_constructor] = []

			# 1.2 Remove all instances of component_constructors from entty in self.component_constructor_to_entities
			self.component_constructor_to_entities[component_constructor].remove(entity)
		
	def remove_components_by_component_constructors_from_all_entities(self,*component_constructors:Type[Component]) -> Set[int]:
		# 1.0 Find entities with any of the component 
		removed_entities_set:Set[int] = set()
		for component_constructor in component_constructors:
			# 1.05 Sanity check
			if not component_constructor in self.component_constructor_to_entities:
				# if DEBUGGING_MODE:  # !@#!@#!@#!@#!@# REMOVE!
				raise Exception(f"ERROR: {component_constructor} does NOT exist in self.component_constructor_to_entities!")
				# Note, but there might not be any entities, just an empty list....
			if len(self.component_constructor_to_entities[component_constructor]) == 0:
				raise Exception(f"ERROR: `{component_constructor}` len(self.component_constructor_to_entities[component_constructor]) == 0")
				# else:
				# 	continue

			# 1.1 Create a set of all entities with component_constructor
			entity_set = self.component_constructor_to_entities[component_constructor]
			removed_entities_set = removed_entities_set.union(entity_set)

			# 1.2 Remove component from entities_to_component_dict
			for entity in entity_set:
				self.entity_to_component_dict[entity][component_constructor].clear()

			# 1.3 remove component from component_constructor_to_entities
			self.component_constructor_to_entities[component_constructor].clear()
		return removed_entities_set

	# #########################################################
	# 					UPDATE
	# #########################################################
	def update(self) -> None:
		# Iterate over all systems
		for system in self.systems:
			system.update(self)

		# Remove components staged for removal
		self._remove_staged_components()

	# #########################################################
	# 				STAGED REMOVAL
	# #########################################################

	def _remove_staged_components(self) -> None:
		# HUGE POTENTIAL FOR OPTIMIZATION


		# 1.0 Iterate over all self.staged_removal_components
		for (component, entity) in self.staged_removal_components_to_entity.items():
			# 1.1 Get type
			component_constructor =  type(component)

			# 1.2 Remove from self.component_constructor_to_entities
			try:
				self.component_constructor_to_entities[component_constructor].remove(entity)
				if len(self.component_constructor_to_entities[component_constructor]) == 0:
					del self.component_constructor_to_entities[component_constructor]
			except Exception as err:
				raise Exception(f"ERROR: {err}. THIS CODE SHOULD NEVER RUN!")

			# 1.3 Remove from self.entity_to_component_obj
			try:
				self.entity_to_component_dict[entity][component_constructor].remove(component)
				if len(self.entity_to_component_dict[entity][component_constructor]) == 0:
					del self.entity_to_component_dict[entity]
			except ValueError as err:
				raise Exception(f"ERROR: {err}. Component was removed from else where. THIS CODE SHOULD NEVER RUN!")
			
		# 2.0 Clear
		self.staged_removal_components_to_entity = {}
		
	# #########################################################
	# 					QUERIES
	# #########################################################

	def does_entity_have_all_component_constructors(self,entity:int,*component_constructors:Type[Component]) -> bool:
		# Note this method is slightly redundant as you could just use `view` instead. However this method is a lot more computationally efficient and more direct at solving its task

		# 0.0 Check if entity even exists
		if not entity in self.entity_to_component_dict:
			raise Exception("ERROR: entity does NOT exist!")

		# 0.5 Check if component constructors even exist in the first place (THIS IS not necessary as some components are rarely added and I will only know once it is added so this is a bad test) SKIP

		# 1.0 check if entity has component_constructors
		for component_constructor in component_constructors:
			if not component_constructor in self.entity_to_component_dict[entity]:
				return False
			else:
				if not entity in self.component_constructor_to_entities[component_constructor]:
					return False
		return True
	

	def do_components_exist(self,*component_constructors:Type[Component]) -> bool:
		"""
			Checks if component INSTANCES of component_constructors exist within <World>. Use before <World>.view(). 
		"""
		for component_constructor in component_constructors:
			if not component_constructor in self.component_constructor_to_entities:
				return False
			else:
				# Check there's at least one entity with component
				if len(self.component_constructor_to_entities[component_constructor]) == 0:
					return False
		return True

	def get_entities_with_component_constructors(self,*component_constructors:Type[Component]) -> Set[int]:
		# Get all entities with these component

		# 0.0 Sanity check
		if not len(component_constructors) == len(set(component_constructors)):
			raise Exception("ERROR: len(component_constructors) == len(set(component_constructors))! You can NOT specify the same component constructor multiple times!")
		if len(component_constructors) == 0:
			raise Exception("ERROR: len(component_constructors) == 0! You must pass in at least one component constructor!")

		# 0.0 Check component_constructors even exist
		# if DEBUGGING_MODE:
		for component_constructor in component_constructors:
			if not component_constructor in self.component_constructor_to_entities:
				raise Exception(f"ERROR: component_constructor `{component_constructor}` does NOT exist in self.component_constructor_to_entities. You can not `view` it!") 
			if len(self.component_constructor_to_entities[component_constructor]) == 0:
				raise Exception(f"ERROR: `{component_constructor}` len(self.component_constructor_to_entities[component_constructor]) == 0")
		

		# 1.0 Create entity sets belonging to each of the component_constructors
		collected_entities : List[Set[int]] = []
		for component_constructor in component_constructors:

			# Check if component_constructor even exists yet
			if not component_constructor in self.component_constructor_to_entities:
				raise Exception("ERROR: THIS CODE SHOULD NEVER BE RUN!")
				# collected_entities.append(set())
				# if DEBUGGING_MODE:
				# 	raise Exception(F"WARNING: {component_constructor} does not exist in self.component_constructor_to_entities") # Could get rid of this. Only here during TESTING phase
			else:
				collected_entities.append(self.component_constructor_to_entities[component_constructor])


		# 2.0 Find the intersection that all the sets have
		intersection_set = collected_entities[0]
		for entity_set in collected_entities[1:]:
			intersection_set = intersection_set.intersection(entity_set)


		return intersection_set

	@overload
	def get_components_from_entity(self, entity: int, cc1: Type[T1], /) -> Tuple[List[T1]]:
		...
	@overload
	def get_components_from_entity(self, entity: int, cc1: Type[T1], cc2: Type[T1], /) -> Tuple[List[T1], List[T2]]:
		...
	@overload
	def get_components_from_entity(self, entity: int, cc1: Type[T1], cc2: Type[T1], cc3: Type[T1], /) -> Tuple[List[T1], List[T2], List[T3]]:
		...
	@overload
	def get_components_from_entity(self, entity: int, cc1: Type[T1], cc2: Type[T1], cc3: Type[T1], cc4: Type[T1], /) -> Tuple[List[T1], List[T2], List[T3], List[T4]]:
		...
	@overload
	def get_components_from_entity(self, entity: int, cc1: Type[T1], cc2: Type[T1], cc3: Type[T1], cc4: Type[T1], cc5: Type[T1], /) -> Tuple[List[T1], List[T2], List[T3], List[T4], List[T5]]:
		...
	@overload
	def get_components_from_entity(self, entity: int, cc1: Type[T1], cc2: Type[T1], cc3: Type[T1], cc4: Type[T1], cc5: Type[T1], cc6: Type[T1], /) -> Tuple[List[T1], List[T2], List[T3], List[T4], List[T5], List[T6]]:
		...
	def get_components_from_entity(self,entity:int, *component_constructors:Type[Component]) -> Any:
			""" 
				Returns component instances of entity
			"""

			# 0.0 Check if entity exists
			if not entity in self.entity_to_component_dict:
				raise Exception(f"ERROR: entity `{entity}` does NOT exist!")
			
			# 0.5 Check if component_constructors exist (You should always check using `does_entity_have_all_component_constructors` first!)
			for component_constructor in component_constructors:
				if not component_constructor in self.component_constructor_to_entities:
					raise Exception(f"ERROR: component_constructor `{component_constructor}` does NOT exist!")
				if len(self.component_constructor_to_entities[component_constructor]) == 0:
					raise Exception(f"ERROR: `{component_constructor}` len(self.component_constructor_to_entities[component_constructor]) == 0")
			# 1.0
			# 1.1 Check i  
			return tuple((self.entity_to_component_dict[entity][component_constructor]) for component_constructor in component_constructors)



	@overload
	def view(self, s1: Type[T1], /) -> List[tuple[int, List[T1]]]:
		...
	@overload
	def view(self, s1: Type[T1], s2: Type[T2], /) -> List[tuple[int, List[T1], List[T2]]]:
		...
	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], /) -> List[tuple[int, List[T1], List[T2], List[T3]]]:
		...
	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], /) -> List[tuple[int, List[T1], List[T2], List[T3], List[T4]]]:
		...
	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], /) -> List[tuple[int, List[T1], List[T2], List[T3], List[T4], List[T5]]]:
		...
	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], /) -> List[tuple[int, List[T1], List[T2], List[T3], List[T4], List[T5], List[T6]]]:
		...
	def view(self,*component_constructors:Type[Component]) -> Any:

		# 1.0 Get all entities with these component
		entity_set = self.get_entities_with_component_constructors(*component_constructors)
		

		# 2.0 get components of entity_set
		view:Any = []
		for entity in entity_set:
			view.append((entity,)+tuple((self.entity_to_component_dict[entity][component_constructor]) for component_constructor in component_constructors))
		return view
		# return tuple((entity, *[self.entity_to_component_dict[entity][component_constructor] for component_constructor in component_constructors]) for entity in entity_set)

		""" 
			examples:
			return [] if no entities used those component constructors
		"""

	



if __name__ == "__main__":
	##############################################################################
	# 						COMPONENT & SYSTEM INSTANCES
	##############################################################################

	class HealthIncrementor(System):
		def __init__(self) -> None:
			super().__init__()

	class Health(Component):
		def __init__(self,value:float) -> None:
			super().__init__()
			self.value:float = value

	class Position(Component):
		def __init__(self, x:float, y:float) -> None:
			super().__init__()
			self.x = x
			self.y = y

	class Armor(Component):
		def __init__(self, value:float) -> None:
			super().__init__()
			self.value:float=value
	

	""""""

	
""" 
	I NEED TO RUN A CHECK ON ALL CODE USING `not component_constructor in self.component_constructor_to_entities`
	"""

""" 
ECS Limitations/Specs:
- Systems can NOT be added or removed after World initialization
- Multiple of the same system can exist
- Multiple of the same component type can exist within the same entity. You can't add the same component instance multiple times

- Use ECS for eventsystem
- You CANOT create entities WITHOUT components
 -> This solves this problem: You can get view of entities WITHOUT components
- Throw error on:  world.view(Health,Position,Position) <- Can't use same component constructor multiple times
"""
