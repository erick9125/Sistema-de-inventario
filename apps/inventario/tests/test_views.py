import pytest


@pytest.mark.django_db
def test_listar_equipo_redirige_sin_sesion(client):
    response = client.get("/listarequipo/")
    assert response.status_code == 302
    assert response.url == "/"


@pytest.mark.django_db
def test_listar_equipo_ok_con_sesion(client):
    session = client.session
    session["uid"] = "fake-token"
    session.save()
    response = client.get("/listarequipo/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_postsign_solo_post(client):
    response = client.get("/postsign/")
    assert response.status_code == 405
