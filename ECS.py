from typing import Dict, List, Set, Tuple, Type

##############################################################################
# 						SYSTEMS
##############################################################################
class System():
	def __init__(self) -> None:
		self.___type___ = "___system___"
	
	def update(self):
		raise Exception("ERROR: Class `{}` has NOT implemented its update() method".format(type(self).__name__))

class HealthIncrementor(System):
	def __init__(self) -> None:
		super().__init__()

##############################################################################
# 						COMPONENTS
##############################################################################
class Component():
	def __init__(self) -> None:
		self.___type___ = "___component___"

class Health(Component):
	def __init__(self,value) -> None:
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

	def add_entity(self,*components:Component):
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

	def remove_entities(self,*entities:int):
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
		component_constructor_set:Set[Type[Component]] = set()
		for entity in entities:
			
			# For each of the component_constructors the entity has, remove this entity from `component_constructor_to_entities`
			for component_constructor in self.entity_to_component_dict[entity]:
				entity_set = self.component_constructor_to_entities[component_constructor]
				entity_set.discard(entity)


		# 2.0 Rememove entities from `entity_to_component_dict`
		for entity in entities:
			self.entity_to_component_dict.pop(entity)

	def add_components_to_entity(self,entity,*components):
		# Adds component(s) from entity
		pass

	def remove_components_from_entity(self):
		# Removes component(s) from entity
		pass

	def update(self):
		# Iterate over all systems
		pass

world = World(HealthIncrementor(),HealthIncrementor())
world.add_entity(Health(10),Health(10),Position(1,2))
world.add_entity(Health(10),Health(10),Position(1,2))
world.add_entity(Health(10),Health(10),Position(1,2),Armor(100))

print(world.entity_to_component_dict)
print(world.component_constructor_to_entities)
world.remove_entities(0)
print(world.entity_to_component_dict)
print(world.component_constructor_to_entities)
world.remove_entities(0)
print(world.entity_to_component_dict)
print(world.component_constructor_to_entities)
""" 
ECS Limitations/Specs:
- Systems can NOT be added or removed after World initialization
- Multiple of the same system can exist
- Multiple of the same component can exist within the same entity

- Use ECS for eventsystem
"""