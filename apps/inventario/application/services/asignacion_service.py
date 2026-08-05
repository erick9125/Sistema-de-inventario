from typing import Iterable, Optional

from apps.inventario.infrastructure.persistence.models import Asignacion
from apps.inventario.infrastructure.persistence.repositories import AsignacionRepository


class AsignacionService:
    def __init__(self, repository: Optional[AsignacionRepository] = None):
        self._repository = repository or AsignacionRepository()

    def listar(self) -> Iterable[Asignacion]:
        return self._repository.list_all()

    def obtener(self, asignacion_id: int) -> Optional[Asignacion]:
        return self._repository.get_by_id(asignacion_id)

    def guardar(self, asignacion: Asignacion) -> Asignacion:
        return self._repository.save(asignacion)

    def eliminar(self, asignacion: Asignacion) -> None:
        self._repository.delete(asignacion)
