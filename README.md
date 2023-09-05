# ecs-python
An entity component system(ECS) made in python

# Usage Examples
```python
from ecs import World, Component, System

class HealthIncrementor(System):
  def update(self,world:World) -> None:
    #world.view(Health)

    #add_entity(Health(10))
    #add_entity(Health(10),Armor(2))

    #health = Health(10)
    #add_component_instances_to_entity(0,health)
    #remove_component_instances_from_entity(0,health)

    #get_entities_with_component_constructors(Health,Armor)

    #remove_components_by_component_constructor_from_entity(Health,Armor)

    #remove_entities(0)
class Health(Component):
	def __init__(self,health:float) -> None:
		self.health = health
class Armor(Component):
	def __init__(self,armor:float) -> None:
		self.armor = armor
```
