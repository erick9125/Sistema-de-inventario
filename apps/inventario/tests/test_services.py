import pytest
from django.contrib.auth.hashers import check_password

from apps.inventario.application.services.equipo_service import EquipoService
from apps.inventario.application.services.usuario_service import UsuarioService
from apps.inventario.infrastructure.persistence.models import Equipo, Usuario
from apps.inventario.presentation.forms import UsuarioForm


@pytest.mark.django_db
def test_equipo_service_crud():
    service = EquipoService()
    equipo = Equipo(
        id=1,
        marca="Dell",
        modelo="Latitude",
        serie="ABC",
        rotulo=10,
        tipo="Notebook",
        descripcion="test",
    )
    service.guardar(equipo)
    assert service.obtener(1).marca == "Dell"
    assert list(service.listar())
    service.eliminar(equipo)
    assert service.obtener(1) is None


@pytest.mark.django_db
def test_usuario_service_and_password_hash():
    form = UsuarioForm(
        data={
            "nombre": "Ana",
            "apellido": "Perez",
            "cargo": "TI",
            "email": "ana@test.com",
            "clave": "secreta123",
        }
    )
    # ModelForm needs instance with pk for IntegerField PK
    form.instance.id = 99
    assert form.is_valid(), form.errors
    user = form.save()
    assert check_password("secreta123", user.clave)

    service = UsuarioService()
    assert service.obtener(99).email == "ana@test.com"
