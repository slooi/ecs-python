import unittest
from ecs import World, Component, System


class Health(Component):
	def __init__(self,health:float) -> None:
		self.health = health
class Armor(Component):
	def __init__(self,armor:float) -> None:
		self.armor = armor



class TestWorld(unittest.TestCase):
	def test_add_entity(self):
		# Basic standard test

		# Setup
		world = World()
		h = Health(1)
		world.add_entity(h)

		self.assertEqual(len(world.component_constructor_to_entities[Health]),1)
		self.assertEqual(world.component_constructor_to_entities[Health].pop(),0)
		self.assertEqual(len(world.component_constructor_to_entities[Health]),0)

		self.assertEqual(len(world.entity_to_component_dict[0][Health]),1)
		self.assertEqual(world.entity_to_component_dict[0][Health].pop(),h)
		self.assertEqual(len(world.entity_to_component_dict[0][Health]),0)

	def test_add_entity__no_component(self):
		world = World()
		try:
			world.add_entity()
		except Exception as err:
			self.assertEqual(str(err),"ERROR: len(components) == 0! You can NOT create an entity with 0 components")

			
		world = World()
		world.add_entity(Armor(10))
		self.assertEqual(len(world.component_constructor_to_entities),1)
		self.assertEqual(len(world.entity_to_component_dict[0][Armor]),1)


	def test_add_entity__same_instance_component(self):
		try:
			world = World()
			h = Health(1)
			world.add_entity(h,h)
			self.fail()
		except Exception as err:
			self.assertEqual(str(err),'ERROR: len(set(components)) == len(components)! You can NOT pass in the same component instance multiple times!')
	

	def test_remove_component_instances_from_entity(self):
		world = World()
		h = Health(1)
		a = Armor(10)
		world.add_entity(h,a)

		world.remove_component_instances_from_entity(0,h)
		# Check health component was removed properly
		self.assertEqual(world.entity_to_component_dict[0][Health],[])
		self.assertEqual(world.component_constructor_to_entities[Health],set())
		# Check Armor component was unaffected
		self.assertEqual(world.entity_to_component_dict[0][Armor][0],a)
		self.assertTrue(0 in world.component_constructor_to_entities[Armor])


	def test_get_entities_with_component_constructors(self):
		world = World()
		world.add_entity(Health(10))
		world.add_entity(Armor(100))
		world.add_entity(Health(10))
		entity_set = world.get_entities_with_component_constructors(Health)

		self.assertEqual(entity_set,{0,2})

	def test_view(self):
		
		world = World()
		world.add_entity(Health(10))
		world.add_entity(Armor(100))
		world.add_entity(Health(10))
		world.add_entity(Armor(100),Health(10),Health(99))

		view = world.view(Health,Armor)
		self.assertEqual(view[0][0],3)
		
		self.assertEqual(view[0][1],world.entity_to_component_dict[3][Health]) 

		self.assertEqual(len(view),1) 


	def test_view_2(self):
		# [(0,list[health],list[armor])]
		world = World()
		world.add_entity(Health(10))
		world.add_entity(Armor(100))
		world.add_entity(Health(10))
		world.add_component_instances_to_entity(0,Armor(-1))

		view = world.view(Health,Armor)
		self.assertEqual(view[0][0],0)
		

		# return [] if no entities used those component constructors
		world = World()
		world.add_entity(Health(10))
		world.add_entity(Armor(100))
		world.add_entity(Health(10))
		world.add_component_instances_to_entity(0,Health(-1))

		view = world.view(Health,Armor)
		self.assertEqual(view,[])

	def test_remove_components_by_component_constructors_from_all_entities(self):	
		world = World()
		world.add_entity(Health(10))
		removed_entities_set = world.remove_components_by_component_constructors_from_all_entities(Health)
		self.assertEqual(removed_entities_set,{0})
		self.assertEqual(len(world.entity_to_component_dict[0][Health]),0)
		self.assertEqual(len(world.component_constructor_to_entities[Health]),0)

		world = World()
		world.add_entity(Health(10))
		try:
			world.remove_components_by_component_constructors_from_all_entities(Armor) # raise exception
		except Exception as err:
			self.assertEqual(str(err),f"ERROR: {Armor} does NOT exist in self.component_constructor_to_entities!")

		world = World()
		world.add_entity(Health(10))
		world.add_entity(Health(10))
		removed_entities_set = world.remove_components_by_component_constructors_from_all_entities(Health)
		self.assertEqual(removed_entities_set == {0,1}								,True)
		self.assertEqual(world.entity_to_component_dict[0][Health] == []			,True)
		self.assertEqual(world.entity_to_component_dict[1][Health] == []			,True)
		self.assertEqual(world.component_constructor_to_entities[Health] == set()	,True)

		world = World()
		world.add_entity(Health(10))
		world.add_entity(Health(10),Armor(10))
		removed_entities_set = world.remove_components_by_component_constructors_from_all_entities(Health)
		removed_entities_set == {0,1}
		self.assertEqual(world.entity_to_component_dict[0][Health] == []				, True)
		self.assertEqual(world.entity_to_component_dict[1][Health] == []				, True)
		self.assertEqual(world.component_constructor_to_entities[Health] == set()		, True)
		self.assertEqual(world.component_constructor_to_entities[Armor] == set([1])		, True)
		self.assertEqual(len(world.entity_to_component_dict[1][Armor]) == 1				, True)


		world = World()
		world.add_entity(Health(10))
		self.assertEqual(world.remove_components_by_component_constructors_from_all_entities() == set()	,True)

		world = World()
		try:
			world.remove_components_by_component_constructors_from_all_entities(Health) # raise exception
		except Exception as err:
			self.assertEqual(str(err),f"ERROR: {Health} does NOT exist in self.component_constructor_to_entities!")

	def test_does_entity_have_all_component_constructors(self):
			
		world = World()
		world.add_entity(Health(10))
		self.assertEqual(world.does_entity_have_all_component_constructors(0,Health),True)

		world = World()
		world.add_entity(Health(10))
		self.assertEqual(world.does_entity_have_all_component_constructors(0,Armor),False)

		world = World()
		world.add_entity(Health(10))
		world.add_entity(Armor(10))
		self.assertEqual(world.does_entity_have_all_component_constructors(0,Armor),False)

		world = World()
		h = Health(10)
		world.add_entity(h)
		world.remove_component_instances_from_entity(0,h) # <- need to change this
		world.add_entity(Armor(10))
		self.assertEqual(world.does_entity_have_all_component_constructors(0,Health),False)

		world = World()
		h = Health(10)
		world.add_entity(h)
		try:
			world.does_entity_have_all_component_constructors(2,Health)
		except Exception as err:
			self.assertEqual(str(err),"ERROR: entity does NOT exist!")

	def test(self):
		world = World()
		world.add_entity(Health(10))
		try:
			world.remove_components_by_component_constructors_from_entity(0,Armor)
		except Exception as err:
			# err
			self.assertEqual(type(err),Exception)

		world = World()
		world.add_entity(Health(10))
		world.remove_components_by_component_constructors_from_entity(0,Health)
		self.assertEqual(world.component_constructor_to_entities[Health] == set()		,True)
		self.assertEqual(world.entity_to_component_dict[0][Health] == []				,True)

	def test_get_components_from_entity(self):
		world = World()
		world.add_entity(Health(10))
		components_view = world.get_components_from_entity(0,Health)
		self.assertEqual(len(components_view) == 1,True)

		world = World()
		world.add_entity(Health(10))
		try:
			world.get_components_from_entity(1,Health)
		except Exception as err:
			self.assertEqual(str(err) == 'ERROR: entity `1` does NOT exist!',True)

		world = World()
		world.add_entity(Health(10))
		try:
			world.get_components_from_entity(0,Armor)
		except Exception as err:
			self.assertEqual(str(err) == "ERROR: component_constructor `<class '__main__.Armor'>` does NOT exist!",True)
	
	def test_do_components_exist(self):
		world = World()
		self.assertEqual(world.do_components_exist(Armor)==False,True)

		world = World()
		world.add_entity(Health(1))
		self.assertEqual(world.do_components_exist(Armor)==False,True)

		world = World()
		world.add_entity(Armor(1))
		self.assertEqual(world.do_components_exist(Armor)==True,True)
		
		world = World()
		world.add_entity(Armor(1))
		world.remove_components_by_component_constructors_from_entity(0,Armor)
		self.assertEqual(world.do_components_exist(Armor)==False,True)

		world = World()
		world.add_entity(Armor(1))
		world.remove_components_by_component_constructors_from_entity(0,Armor)
		world.add_component_instances_to_entity(0,Armor(0))
		self.assertEqual(world.do_components_exist(Armor)==True,True)

		world = World()
		world.add_entity(Armor(1))
		world.remove_components_by_component_constructors_from_entity(0,Armor)
		world.add_component_instances_to_entity(0,Health(0))
		self.assertEqual(world.do_components_exist(Armor)==False,True)

	def test_stage_remove_component_instances_from_entity(self):
		world = World()
		try:
			world.stage_remove_component_instances_from_entity(0,Armor(1))
		except Exception as err:
			self.assertEqual(True,True)

		world = World()
		world.add_entity(Health(1))
		try:
			world.stage_remove_component_instances_from_entity(0,Armor(1))
		except Exception as err:
			self.assertEqual(True,True)

		world = World()
		world.add_entity(Health(1))
		try:
			world.stage_remove_component_instances_from_entity(0,Health(1))
		except Exception as err:
			self.assertEqual(True,True)

		world = World()
		h = Health(1)
		world.add_entity(h)
		world.stage_remove_component_instances_from_entity(0,h)
		print(len(world.staged_removal_components_to_entity.keys())==1)


	def test_stage_remove_components_by_component_constructors_from_entity(self):
	
		world = World()
		try:
			world.stage_remove_components_by_component_constructors_from_entity(0,Health)
		except Exception as err:
			self.assertEqual(True,True)
		# entity err

		world = World()
		world.add_entity(Armor(1))
		try:
			world.stage_remove_components_by_component_constructors_from_entity(0,Health)
		except Exception as err:
			self.assertEqual(True,True)
		# health err

		world = World()
		world.add_entity(Armor(1))
		world.remove_components_by_component_constructors_from_all_entities(Armor)
		try:
			world.stage_remove_components_by_component_constructors_from_entity(0,Armor)
		except Exception as err:
			self.assertEqual(True,True)

		world = World()
		world.add_entity(Armor(1))
		world.stage_remove_components_by_component_constructors_from_entity(0,Armor)
		self.assertEqual(len(world.staged_removal_components_to_entity.keys()) == 1,True)

		world = World()
		world.add_entity(Armor(1))
		world.add_entity(Armor(1))
		world.stage_remove_components_by_component_constructors_from_entity(0,Armor)
		self.assertEqual(len(world.staged_removal_components_to_entity.keys()) == 1,True)

		world = World()
		world.add_entity(Armor(1),Armor(1))
		world.add_entity(Armor(1))
		world.stage_remove_components_by_component_constructors_from_entity(0,Armor)
		self.assertEqual(len(world.staged_removal_components_to_entity.keys()) == 2,True)

		world = World()
		world.add_entity(Health(1),Armor(1))
		world.add_entity(Armor(1))
		world.stage_remove_components_by_component_constructors_from_entity(0,Health)
		self.assertEqual(len(world.staged_removal_components_to_entity.keys()) == 1,True)

	def test_stage_remove_components_by_component_constructors_from_all_entities(self):
		world = World()
		world.add_entity(Armor(1))
		try:
			world.stage_remove_components_by_component_constructors_from_all_entities(Health)
		except Exception as err:
			self.assertEqual(True,True)
			# Err

		world = World()
		world.add_entity(Health(1))
		world.remove_components_by_component_constructors_from_entity(0,Health)
		try:
			world.stage_remove_components_by_component_constructors_from_all_entities(Health)
		except Exception as err:
			self.assertEqual(True,True)
			# Err
		
		world = World()
		world.add_entity(Health(1))
		world.stage_remove_components_by_component_constructors_from_all_entities(Health)
		self.assertEqual(len(world.staged_removal_components_to_entity.keys()) == 1,True)

		
		world = World()
		world.add_entity(Health(1),Health(1))
		world.stage_remove_components_by_component_constructors_from_all_entities(Health)
		self.assertEqual(len(world.staged_removal_components_to_entity.keys()) == 2,True)
		
		world = World()
		world.add_entity(Health(1),Armor(1))
		world.stage_remove_components_by_component_constructors_from_all_entities(Health)
		world.stage_remove_components_by_component_constructors_from_all_entities(Armor)
		self.assertEqual(len(world.staged_removal_components_to_entity.keys()) == 2,True)
		
		world = World()
		world.add_entity(Health(1),Armor(1))
		world.remove_components_by_component_constructors_from_all_entities(Health)
		try:
			world.stage_remove_components_by_component_constructors_from_all_entities(Health)
			world.stage_remove_components_by_component_constructors_from_all_entities(Armor)
		except Exception as err:
			self.assertEqual(True,True)

	def test__remove_staged_components(self):
		world = World()
		world.add_entity(Armor(1))
		world.stage_remove_components_by_component_constructors_from_all_entities(Armor)
		world.update()
		self.assertEqual(len(world.staged_removal_components_to_entity)==0,True)
		self.assertEqual(world.component_constructor_to_entities,{})
		self.assertEqual(world.entity_to_component_dict,{0:{}})

		world = World()
		world.add_entity(Armor(1))
		world.stage_remove_components_by_component_constructors_from_all_entities(Armor)
		world.update()
		world.add_entity(Armor(1))
		world.stage_remove_components_by_component_constructors_from_all_entities(Armor)
		world.update()
		self.assertEqual(len(world.staged_removal_components_to_entity)==0,True)
		self.assertEqual(world.component_constructor_to_entities,{})
		self.assertEqual(world.entity_to_component_dict,{0:{},1:{}})

if __name__ == "__main__":
	unittest.main()
		# world = World()
		# world.add_entity(Health(10))
		# world.remove_components_by_component_constructors_from_all_entities() # <- need to change this
		# world.add_entity(Armor(10))
		# print(world.does_entity_have_all_component_constructors(0,Health)==False)
