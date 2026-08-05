from typing import Generic, Iterable, Optional, Protocol, TypeVar

T = TypeVar("T")


class Repository(Protocol, Generic[T]):
    def get_by_id(self, entity_id: int) -> Optional[T]:
        ...

    def list_all(self) -> Iterable[T]:
        ...

    def save(self, entity: T) -> T:
        ...

    def delete(self, entity: T) -> None:
        ...


class EquipoRepository(Repository[object], Protocol):
    pass


class AsignacionRepository(Repository[object], Protocol):
    pass


class PdaRepository(Repository[object], Protocol):
    pass


class TelefonoRepository(Repository[object], Protocol):
    pass


class UsuarioRepository(Repository[object], Protocol):
    pass
