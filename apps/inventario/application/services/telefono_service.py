from typing import Iterable, Optional

from apps.inventario.infrastructure.persistence.models import Telefono
from apps.inventario.infrastructure.persistence.repositories import TelefonoRepository


class TelefonoService:
    def __init__(self, repository: Optional[TelefonoRepository] = None):
        self._repository = repository or TelefonoRepository()

    def listar(self) -> Iterable[Telefono]:
        return self._repository.list_all()

    def obtener(self, telefono_id: int) -> Optional[Telefono]:
        return self._repository.get_by_id(telefono_id)

    def guardar(self, telefono: Telefono) -> Telefono:
        return self._repository.save(telefono)

    def eliminar(self, telefono: Telefono) -> None:
        self._repository.delete(telefono)
