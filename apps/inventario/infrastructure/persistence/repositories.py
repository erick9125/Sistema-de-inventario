from typing import Iterable, Optional, Type, TypeVar

from django.db import models

from apps.inventario.infrastructure.persistence.models import (
    Asignacion,
    Equipo,
    Pda,
    Telefono,
    Usuario,
)

T = TypeVar("T", bound=models.Model)


class DjangoRepository:
    model: Type[models.Model]

    def get_by_id(self, entity_id: int) -> Optional[models.Model]:
        return self.model.objects.filter(pk=entity_id).first()

    def list_all(self) -> Iterable[models.Model]:
        return self.model.objects.all()

    def save(self, entity: models.Model) -> models.Model:
        entity.save()
        return entity

    def delete(self, entity: models.Model) -> None:
        entity.delete()


class EquipoRepository(DjangoRepository):
    model = Equipo


class AsignacionRepository(DjangoRepository):
    model = Asignacion


class PdaRepository(DjangoRepository):
    model = Pda


class TelefonoRepository(DjangoRepository):
    model = Telefono


class UsuarioRepository(DjangoRepository):
    model = Usuario
