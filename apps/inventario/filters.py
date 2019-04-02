import django_filters
from apps.inventario.models import usuario,equipo,asignacion,pda,telefono

class equipoFilter(django_filters.FilterSet):

    CHOICES=(
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )
    ordering = django_filters.ChoiceFilter(label='ordering',choice=CHOICES, method='filter_by_ordering')

    class Meta:
        model = equipo
        fields = {
            'modelo': ['icontains'],
            'serie' : ['icontains'],
            'fecha_ing' : ['icontains']
            }

    def filter_by_ordering(self,queryset,name,value):
        expression = 'fecha_ing' if value == 'ascending' else '-fecha_ing'
        return queryset.order_by(expression)