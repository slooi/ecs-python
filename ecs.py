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


##############################################################################
# 						COMPONENT
##############################################################################

class Component():
	pass


##############################################################################
# 						WORLD
##############################################################################

T = TypeVar("T")
T1 = TypeVar("T1", bound=Component)
T2 = TypeVar("T2", bound=Component)
T3 = TypeVar("T3", bound=Component)
T4 = TypeVar("T4", bound=Component)
T5 = TypeVar("T5", bound=Component)

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
		self.entity_to_component_dict : Dict[int,Dict[Type[Component],List[Component]]] = {} # Note that entities can have multiple of the SAME component
		self.component_constructor_to_entities : Dict[Type[Component],Set[int]] = {}

	# #########################################################
	# 					ENTITIES
	# #########################################################
	def add_entity(self,*components:Component) -> int:

		# 0.0 Check that there are no duplicate component instances
		if not len(set(components)) == len(components):
			raise Exception("ERROR: len(set(components)) == len(components)! You can NOT pass in the same component instance multiple times!")
		if len(components) == 0:
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
	# 					COMPONENTS
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
			component_list = self.entity_to_component_dict[entity][component_constructor]
			if not component in component_list:
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


	# #########################################################
	# 					UPDATE
	# #########################################################
	def update(self):
		# Iterate over all systems
		for system in self.systems:
			system.update(self)

	# #########################################################
	# 					QUERIES
	# #########################################################
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

		
	def remove_components_by_component_constructor_from_entity(self):
		pass

	def does_entity_has_components_constructor(self):
		# Note this method is slightly redundant as you could just use `view` instead. However this method is a lot more computationally efficient and more direct at solving its task

		pass

	def get_entities_with_component_constructors(self,*component_constructors:Type[Component]) -> Set[int]:
		# Get all entities with these component

		# 0.0 Sanity check
		if not len(component_constructors) == len(set(component_constructors)):
			raise Exception("ERROR: len(component_constructors) == len(set(component_constructors))! You can NOT specify the same component constructor multiple times!")


		# 0.0 Check component_constructors even exist
		for component_constructor in component_constructors:
			if not component_constructor in self.component_constructor_to_entities:
				raise Exception(f"ERROR: component_constructor `{component_constructor}` does NOT exist in self.component_constructor_to_entities. You can not `view` it!") 

		

		# 1.0 Create entity sets belonging to each of the component_constructors
		collected_entities : List[Set[int]] = []
		for component_constructor in component_constructors:

			# Check if component_constructor even exists yet
			if not component_constructor in self.component_constructor_to_entities:
				collected_entities.append(set())
				if DEBUGGING_MODE:
					raise Exception(F"WARNING: {component_constructor} does not exist in self.component_constructor_to_entities") # Could get rid of this. Only here during TESTING phase
			else:
				collected_entities.append(self.component_constructor_to_entities[component_constructor])


		# 2.0 Find the intersection that all the sets have
		intersection_set = collected_entities[0]
		for entity_set in collected_entities[1:]:
			intersection_set = intersection_set.intersection(entity_set)


		return intersection_set
	



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

	world = World(HealthIncrementor(),HealthIncrementor())
	world.add_entity(Health(10))
	world.add_entity(Armor(100))
	world.add_entity(Health(10))
	world.add_entity(Armor(100),Health(10),Health(99))
	b = world.view(Health,Armor)
""" 
ECS Limitations/Specs:
- Systems can NOT be added or removed after World initialization
- Multiple of the same system can exist
- Multiple of the same component type can exist within the same entity. You can't add the same component instance multiple times

- Use ECS for eventsystem
- You can create entities WITHOUT components
 -> You can get view of entities WITHOUT components
- Throw error on:  world.view(Health,Position,Position) <- Can't use same component constructor multiple times
"""
