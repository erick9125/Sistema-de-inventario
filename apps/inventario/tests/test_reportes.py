import pytest

from apps.inventario.application.services.reporte_service import ReporteService
from apps.inventario.infrastructure.persistence.models import Equipo


@pytest.mark.django_db
def test_reporte_equipos_excel():
    Equipo.objects.create(
        id=1,
        marca="HP",
        modelo="Elite",
        serie="S1",
        rotulo=1,
        tipo="PC",
        descripcion="demo",
    )
    response = ReporteService().equipos()
    assert response.status_code == 200
    assert "spreadsheetml" in response["Content-Type"]
    assert "ReporteEquipoExcel.xlsx" in response["Content-Disposition"]
