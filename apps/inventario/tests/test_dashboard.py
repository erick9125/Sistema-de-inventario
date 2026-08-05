import pytest

from apps.inventario.application.services.dashboard_service import DashboardService
from apps.inventario.infrastructure.persistence.models import Equipo, Pda, Telefono


@pytest.mark.django_db
def test_dashboard_service_counts():
    Equipo.objects.create(
        id=1, marca="HP", modelo="E", serie="1", rotulo=1, tipo="PC", descripcion="x"
    )
    Pda.objects.create(
        id=1,
        ot="1",
        modelo_pda="M",
        serie_pda="S",
        serie_bateria="B",
        num_inventario="N",
        sucursal="S",
        region="R",
        estado="OK",
        descripcion_pda="d",
    )
    Telefono.objects.create(
        id=1,
        marca_tel="A",
        modelo_tel="B",
        serie_tel="C",
        numero_tel=123,
        usuario_asig_tel="u",
        departamento_usuario="d",
    )
    stats = DashboardService().obtener_estadisticas()
    assert stats.equipos == 1
    assert stats.pdas == 1
    assert stats.telefonos == 1
    assert stats.total >= 3


@pytest.mark.django_db
def test_dashboard_requiere_sesion(client):
    response = client.get("/dashboard/")
    assert response.status_code == 302
    assert response.url == "/"


@pytest.mark.django_db
def test_dashboard_ok_con_sesion(client):
    session = client.session
    session["uid"] = "token"
    session["email"] = "demo@inventario.local"
    session.save()
    response = client.get("/dashboard/")
    assert response.status_code == 200
    assert b"Dashboard" in response.content
