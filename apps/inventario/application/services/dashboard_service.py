from dataclasses import dataclass

from apps.inventario.infrastructure.persistence.models import (
    Asignacion,
    Equipo,
    Pda,
    Telefono,
    Usuario,
)


@dataclass(frozen=True)
class DashboardStats:
    equipos: int
    asignaciones: int
    pdas: int
    telefonos: int
    usuarios: int

    @property
    def total(self) -> int:
        return self.equipos + self.asignaciones + self.pdas + self.telefonos + self.usuarios


class DashboardService:
    def obtener_estadisticas(self) -> DashboardStats:
        return DashboardStats(
            equipos=Equipo.objects.count(),
            asignaciones=Asignacion.objects.count(),
            pdas=Pda.objects.count(),
            telefonos=Telefono.objects.count(),
            usuarios=Usuario.objects.count(),
        )
