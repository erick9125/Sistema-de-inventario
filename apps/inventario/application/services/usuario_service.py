from typing import Iterable, Optional

from apps.inventario.infrastructure.persistence.models import Usuario
from apps.inventario.infrastructure.persistence.repositories import UsuarioRepository


class UsuarioService:
    def __init__(self, repository: Optional[UsuarioRepository] = None):
        self._repository = repository or UsuarioRepository()

    def listar(self) -> Iterable[Usuario]:
        return self._repository.list_all()

    def obtener(self, usuario_id: int) -> Optional[Usuario]:
        return self._repository.get_by_id(usuario_id)

    def guardar(self, usuario: Usuario) -> Usuario:
        return self._repository.save(usuario)

    def eliminar(self, usuario: Usuario) -> None:
        self._repository.delete(usuario)
