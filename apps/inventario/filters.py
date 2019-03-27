import django_filters
from apps.inventario.models import usuario,equipo,asignacion,pda,telefono

class jugadorFilter(django_filters.FilterSet):
    class Meta:
        model = usuario
        fields = ['id', 'nombre', 'email']