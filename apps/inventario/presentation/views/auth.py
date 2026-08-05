from django.contrib import auth, messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from apps.inventario.application.container import get_auth_service
from apps.inventario.application.services.dashboard_service import DashboardService
from apps.inventario.domain.exceptions import AuthNoConfigurado, CredencialesInvalidas
from apps.inventario.presentation.mixins import firebase_login_required

DASHBOARD_URL = "/dashboard/"


def sing_in(request):
    if get_auth_service().is_authenticated(request.session):
        return redirect(DASHBOARD_URL)
    return render(request, "home/homeLogin.html")


@require_http_methods(["POST"])
def post_sign(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    auth_service = get_auth_service()
    try:
        auth_service.login(email, password, request.session)
    except (CredencialesInvalidas, AuthNoConfigurado) as exc:
        messages.error(request, str(exc))
        return redirect("/")

    messages.success(request, f"Bienvenido, {email}")
    return redirect(DASHBOARD_URL)


def logout_view(request):
    get_auth_service().logout(request.session)
    auth.logout(request)
    messages.info(request, "Sesion cerrada correctamente")
    return redirect("/")


@firebase_login_required
def dashboard(request):
    stats = DashboardService().obtener_estadisticas()
    return render(
        request,
        "home/dashboard.html",
        {
            "stats": stats,
            "e": request.session.get("email", ""),
        },
    )


@firebase_login_required
def informe(request):
    return render(request, "informe/informe.html")


singIn = sing_in
postsign = post_sign
logout = logout_view
