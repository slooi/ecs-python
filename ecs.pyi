from _typeshed import Incomplete
from typing import Any, Dict, Set, Tuple, Type, TypeVar
from typing import Any, List, Set, Type, TypeVar, overload

T = TypeVar('T')
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
T11 = TypeVar("T11", bound=Component)
T12 = TypeVar("T12", bound=Component)
T13 = TypeVar("T13", bound=Component)
T14 = TypeVar("T14", bound=Component)
T15 = TypeVar("T15", bound=Component)
T16 = TypeVar("T16", bound=Component)
T17 = TypeVar("T17", bound=Component)
T18 = TypeVar("T18", bound=Component)
T19 = TypeVar("T19", bound=Component)
T20 = TypeVar("T20", bound=Component)
T21 = TypeVar("T21", bound=Component)
T22 = TypeVar("T22", bound=Component)
T23 = TypeVar("T23", bound=Component)
T24 = TypeVar("T24", bound=Component)
T25 = TypeVar("T25", bound=Component)
T26 = TypeVar("T26", bound=Component)
T27 = TypeVar("T27", bound=Component)
T28 = TypeVar("T28", bound=Component)
T29 = TypeVar("T29", bound=Component)
T30 = TypeVar("T30", bound=Component)
DEBUGGING_MODE: bool

class System:
	def update(self, world: World) -> None: ...

class Component: 
	def pp(self) -> None: ...

class World:
	entity_counter : int
	systems : Tuple[System,...]
	entity_to_component_dict : Dict[int,Dict[Type[Component],List[Component]]]
	component_constructor_to_entities : Dict[Type[Component],Set[int]]
	def __init__(self, *systems: System) -> None: ...
	def add_entity(self, *components: Component) -> int: ...
	def remove_entities(self, *entities: int) -> None: ...
	def add_component_instances_to_entity(self, entity: int, *components: Component) -> None: ...
	def remove_component_instances_from_entity(self, entity: int, *components: Component) -> None: ...
	def update(self) -> None: ...
	def get_entities_with_component_constructors(self, *component_constructors: Type[Component]) -> Set[int]: ...
	def remove_components_by_component_constructors_from_all_entities(self,*component_constructors:Type[Component]) -> Set[int]: ...
	def does_entity_have_all_component_constructors(self,entity:int,*component_constructors:Type[Component]) -> bool: ...
	def remove_components_by_component_constructors_from_entity(self,entity:int,*component_constructors:Type[Component]) -> None: ...
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

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], /) -> List[tuple[int, List[T1], List[T2], List[T3], List[T4], List[T5], List[T6], List[T7]]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], /) -> List[tuple[int, List[T1], List[T2], List[T3], List[T4], List[T5], List[T6], List[T7], List[T8]]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], /) -> List[tuple[int, List[T1], List[T2], List[T3], List[T4], List[T5], List[T6], List[T7], List[T8], List[T9]]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], /) -> List[tuple[int, List[T1], List[T2], List[T3], List[T4], List[T5], List[T6], List[T7], List[T8], List[T9], List[T10]]]:
		...
