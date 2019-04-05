import django_filters
from apps.inventario.models import usuario,equipo,asignacion,pda,telefono

class equipoFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(equipoFilter, self).__init__(*args, **kwargs)
        self.filters['modelo'].label = 'Modelo :'
        self.filters['serie'].label = 'Serie :'
        self.filters['fecha_ing'].label = 'Fecha de ingreso :'

    class Meta:
        model = equipo
        fields = [
            'modelo', 'serie', 'fecha_ing'
        ]
        
        
class asignacionFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(asignacionFilter, self).__init__(*args, **kwargs)
        self.filters['usuario_asig'].label = 'Usuario Asignado :'
        self.filters['fecha_entrega'].label = 'Fecha de entrega :'
        self.filters['serie_equipo_asig'].label = 'Serie del equipo asignado :'
        
    class Meta:
        model = asignacion
        fields = [
            'usuario_asig', 'fecha_entrega', 'serie_equipo_asig'
        ]


class pdaFilter(django_filters.FilterSet):
    def __init__(self, *args,**kwargs):
        super(pdaFilter, self).__init__(*args,**kwargs)
        self.filters['serie_pda'].label = 'Serie PDA :'
        self.filters['fecha_ing'].label = 'Fecha de ingreso :'
        
    class Meta:
        model = pda
        fields =[
            'serie_pda','fecha_ing'
        ]

class telefonoFilter(django_filters.FilterSet):
    def __init__(self,*args,**kwargs):
        super(telefonoFilter,self).__init__(*args,**kwargs)
        self.filters['serie_tel'].label = 'Serie o IMEI del teléfono :'
        self.filters['numero_tel'].label = 'Número de teléfono :'
        self.filters['fecha_ing_tel'].label = 'Fecha de ingreso :'

    class Meta:
        model = telefono
        fields = [
            'serie_tel', 'numero_tel' , 'fecha_ing_tel'
        ]