from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.inventario.urls")),
    re_path(r"^usuario/", include(("apps.inventario.urls", "usuario"), namespace="usuario")),
    re_path(r"^equipo/", include(("apps.inventario.urls", "equipos"), namespace="equipos")),
    re_path(r"^asignacion/", include(("apps.inventario.urls", "Asignacion"), namespace="Asignacion")),
    re_path(r"^pda/", include(("apps.inventario.urls", "pda"), namespace="pda")),
    re_path(r"^telefono/", include(("apps.inventario.urls", "telefono"), namespace="telefono")),
]
