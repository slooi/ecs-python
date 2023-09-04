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

class Component: ...

class HealthIncrementor(System):
	def __init__(self) -> None: ...

class Health(Component):
	value: Incomplete
	def __init__(self, value: float) -> None: ...

class Position(Component):
	x: Incomplete
	y: Incomplete
	def __init__(self, x: float, y: float) -> None: ...

class Armor(Component):
	value: Incomplete
	def __init__(self, value: float) -> None: ...

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
	def remove_components_by_component_constructor_from_entity(self) -> None: ...
	def does_entity_has_components_constructor(self) -> None: ...
	def get_entities_with_component_constructors(self, *component_constructors: Type[Component]) -> Set[int]: ...
	
	@overload
	def view(self, s1: Type[T1], /) -> List[tuple[int, T1]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], /) -> List[tuple[int, T1, T2]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], /) -> List[tuple[int, T1, T2, T3]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], /) -> List[tuple[int, T1, T2, T3, T4]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], /) -> List[tuple[int, T1, T2, T3, T4, T5]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13]]:
		...
		
	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16]]:
		...
	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], s17: Type[T17], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], s17: Type[T17], s18: Type[T18], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], s17: Type[T17], s18: Type[T18], s19: Type[T19], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19]]:
		...
	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], s17: Type[T17], s18: Type[T18], s19: Type[T19], s20: Type[T20], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], s17: Type[T17], s18: Type[T18], s19: Type[T19], s20: Type[T20], s21: Type[T21], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], s17: Type[T17], s18: Type[T18], s19: Type[T19], s20: Type[T20], s21: Type[T21], s22: Type[T22], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21, T22]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], s17: Type[T17], s18: Type[T18], s19: Type[T19], s20: Type[T20], s21: Type[T21], s22: Type[T22], s23: Type[T23], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21, T22, T23]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], s17: Type[T17], s18: Type[T18], s19: Type[T19], s20: Type[T20], s21: Type[T21], s22: Type[T22], s23: Type[T23], s24: Type[T24], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21, T22, T23, T24]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], s17: Type[T17], s18: Type[T18], s19: Type[T19], s20: Type[T20], s21: Type[T21], s22: Type[T22], s23: Type[T23], s24: Type[T24], s25: Type[T25], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21, T22, T23, T24, T25]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], s17: Type[T17], s18: Type[T18], s19: Type[T19], s20: Type[T20], s21: Type[T21], s22: Type[T22], s23: Type[T23], s24: Type[T24], s25: Type[T25], s26: Type[T26], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21, T22, T23, T24, T25, T26]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], s17: Type[T17], s18: Type[T18], s19: Type[T19], s20: Type[T20], s21: Type[T21], s22: Type[T22], s23: Type[T23], s24: Type[T24], s25: Type[T25], s26: Type[T26], s27: Type[T27], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21, T22, T23, T24, T25, T26, T27]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], s17: Type[T17], s18: Type[T18], s19: Type[T19], s20: Type[T20], s21: Type[T21], s22: Type[T22], s23: Type[T23], s24: Type[T24], s25: Type[T25], s26: Type[T26], s27: Type[T27], s28: Type[T28], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21, T22, T23, T24, T25, T26, T27, T28]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], s17: Type[T17], s18: Type[T18], s19: Type[T19], s20: Type[T20], s21: Type[T21], s22: Type[T22], s23: Type[T23], s24: Type[T24], s25: Type[T25], s26: Type[T26], s27: Type[T27], s28: Type[T28], s29: Type[T29], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21, T22, T23, T24, T25, T26, T27, T28, T29]]:
		...

	@overload
	def view(self, s1: Type[T1], s2: Type[T2], s3: Type[T3], s4: Type[T4], s5: Type[T5], s6: Type[T6], s7: Type[T7], s8: Type[T8], s9: Type[T9], s10: Type[T10], s11: Type[T11], s12: Type[T12], s13: Type[T13], s14: Type[T14], s15: Type[T15], s16: Type[T16], s17: Type[T17], s18: Type[T18], s19: Type[T19], s20: Type[T20], s21: Type[T21], s22: Type[T22], s23: Type[T23], s24: Type[T24], s25: Type[T25], s26: Type[T26], s27: Type[T27], s28: Type[T28], s29: Type[T29], s30: Type[T30], /) -> List[tuple[int, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21, T22, T23, T24, T25, T26, T27, T28, T29, T30]]:
		...
