from django.contrib import admin

from apps.inventario.infrastructure.persistence.models import (
    Asignacion,
    Equipo,
    Pda,
    Telefono,
    Usuario,
)

admin.site.register(Equipo)
admin.site.register(Asignacion)
admin.site.register(Telefono)
admin.site.register(Pda)
admin.site.register(Usuario)
