import django_filters
from apps.inventario.models import usuario,equipo,asignacion,pda,telefono

class equipoFilter(django_filters.FilterSet):


    class Meta:
        model = equipo
        fields = [
            'modelo', 'serie', 'fecha_ing'
        ]
        
