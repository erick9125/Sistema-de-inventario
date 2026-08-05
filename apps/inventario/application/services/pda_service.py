from typing import Iterable, Optional

from apps.inventario.infrastructure.persistence.models import Pda
from apps.inventario.infrastructure.persistence.repositories import PdaRepository


class PdaService:
    def __init__(self, repository: Optional[PdaRepository] = None):
        self._repository = repository or PdaRepository()

    def listar(self) -> Iterable[Pda]:
        return self._repository.list_all()

    def obtener(self, pda_id: int) -> Optional[Pda]:
        return self._repository.get_by_id(pda_id)

    def guardar(self, pda: Pda) -> Pda:
        return self._repository.save(pda)

    def eliminar(self, pda: Pda) -> None:
        self._repository.delete(pda)
