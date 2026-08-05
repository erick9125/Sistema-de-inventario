from django.contrib import auth
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from apps.inventario.application.container import get_auth_service
from apps.inventario.domain.exceptions import AuthNoConfigurado, CredencialesInvalidas
from apps.inventario.presentation.mixins import firebase_login_required


def sing_in(request):
    if get_auth_service().is_authenticated(request.session):
        return redirect("/listarequipo/")
    return render(request, "home/homeLogin.html")


@require_http_methods(["POST"])
def post_sign(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    auth_service = get_auth_service()
    try:
        auth_service.login(email, password, request.session)
    except (CredencialesInvalidas, AuthNoConfigurado) as exc:
        return render(request, "home/homeLogin.html", {"messg": str(exc)})

    return render(request, "home/home.html", {"e": email})


def logout_view(request):
    get_auth_service().logout(request.session)
    auth.logout(request)
    return redirect("/")


@firebase_login_required
def informe(request):
    return render(request, "informe/informe.html")


# Compatibilidad con nombres antiguos
singIn = sing_in
postsign = post_sign
logout = logout_view
