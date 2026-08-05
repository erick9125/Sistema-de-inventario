from typing import Iterable, Optional

from apps.inventario.infrastructure.persistence.models import Equipo
from apps.inventario.infrastructure.persistence.repositories import EquipoRepository


class EquipoService:
    def __init__(self, repository: Optional[EquipoRepository] = None):
        self._repository = repository or EquipoRepository()

    def listar(self) -> Iterable[Equipo]:
        return self._repository.list_all()

    def obtener(self, equipo_id: int) -> Optional[Equipo]:
        return self._repository.get_by_id(equipo_id)

    def guardar(self, equipo: Equipo) -> Equipo:
        return self._repository.save(equipo)

    def eliminar(self, equipo: Equipo) -> None:
        self._repository.delete(equipo)
