import django_filters

from apps.inventario.infrastructure.persistence.models import Asignacion, Equipo, Pda, Telefono


class EquipoFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters["modelo"].label = "Modelo :"
        self.filters["serie"].label = "Serie :"
        self.filters["fecha_ing"].label = "Fecha de ingreso :"

    class Meta:
        model = Equipo
        fields = ["modelo", "serie", "fecha_ing"]


class AsignacionFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters["usuario_asig"].label = "Usuario Asignado :"
        self.filters["fecha_entrega"].label = "Fecha de entrega :"
        self.filters["serie_equipo_asig"].label = "Serie del equipo asignado :"

    class Meta:
        model = Asignacion
        fields = ["usuario_asig", "fecha_entrega", "serie_equipo_asig"]


class PdaFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters["serie_pda"].label = "Serie PDA :"
        self.filters["fecha_ing"].label = "Fecha de ingreso :"

    class Meta:
        model = Pda
        fields = ["serie_pda", "fecha_ing"]


class TelefonoFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters["serie_tel"].label = "Serie o IMEI del teléfono :"
        self.filters["numero_tel"].label = "Número de teléfono :"
        self.filters["fecha_ing_tel"].label = "Fecha de ingreso :"

    class Meta:
        model = Telefono
        fields = ["serie_tel", "numero_tel", "fecha_ing_tel"]


equipoFilter = EquipoFilter
asignacionFilter = AsignacionFilter
pdaFilter = PdaFilter
telefonoFilter = TelefonoFilter
