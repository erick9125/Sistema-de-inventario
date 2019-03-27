from django import forms
from apps.inventario.models import usuario , asignacion , equipo , pda , telefono

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = [
            'nombre',
            'apellido',
            'cargo',
            'email',
            'clave',
        ]

        labels = {
            'nombre' : 'Nombre',
            'apellido': 'Apellido',
            'cargo' : 'Cargo',
            'email' : 'Email',
            'clave' : 'Contraseña',
        }

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'apellido' : forms.TextInput(attrs={'class':'form-control'}),
            'cargo' : forms.TextInput(attrs={'class':'form-control'}),
            'email' :forms.TextInput(attrs={'class':'form-control'}),
            'clave' :forms.TextInput(attrs={'class':'form-control'}),
        }

class EquipoForm(forms.ModelForm):
    class Meta:
        model = equipo
        fields = [
            'marca',
            'modelo', 
            'serie',
            'rotulo',
            'fecha_ing',
            'tipo',
            'activo',
            'descripcion',
        ]

        labels = {
            'marca' : 'Marca',
            'modelo' : 'Modelo', 
            'serie' : 'Serie',
            'rotulo' : 'Rotulo',
            'fecha_ing' : 'Fecha de ingreso',
            'tipo' : 'Tipo',
            'activo' : 'Activo',
            'descripcion' : 'Descripción',
        }

        widgets = {
            'marca' :forms.TextInput(attrs={'class':'form-control'}),
            'modelo':forms.TextInput(attrs={'class':'form-control'}), 
            'serie' :forms.TextInput(attrs={'class':'form-control'}),
            'rotulo' :forms.TextInput(attrs={'class':'form-control'}),
            'fecha_ing' :forms.DateInput(attrs={'class':'form-control'}),
            'tipo' :forms.TextInput(attrs={'class':'form-control'}),
            'activo' :forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control'}),
        }

class asignacionForm(forms.ModelForm):
    class Meta:
        model = asignacion
        fields = [
            'usuario_asig',
            'cargo',
            'departamento',
            'fecha_entrega',
            'marca_equipo_asig',
            'modelo_equipo_asig',
            'serie_equipo_asig',
            'rotulo_equipo_asig',
            'tipo_equipo',
            'activo',
        ]

        labels = {
            'usuario_asig' : 'Usuario Asignado',
            'cargo' : 'Cargo',
            'departamento' : 'Departamento',
            'fecha_entrega' : 'Fecha de entrega',
            'marca_equipo_asig': 'Marca de equipo asignado',
            'modelo_equipo_asig' : 'Modelo de equipo asignado',
            'serie_equipo_asig' : 'Serie de equipo asignado',
            'rotulo_equipo_asig' : 'Rotulo de equipo asignado',
            'tipo_equipo' : 'Tipo de equipo',
            'activo' : 'Activo',
        }

        widgets = {
            'usuario_asig' :forms.TextInput(attrs={'class':'form-control'}),
            'cargo':forms.TextInput(attrs={'class':'form-control'}),
            'departamento':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_entrega':forms.DateInput(attrs={'class':'form-control'}),
            'marca_equipo_asig':forms.TextInput(attrs={'class':'form-control'}),
            'modelo_equipo_asig':forms.TextInput(attrs={'class':'form-control'}),
            'serie_equipo_asig':forms.TextInput(attrs={'class':'form-control'}),
            'rotulo_equipo_asig':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_equipo':forms.TextInput(attrs={'class':'form-control'}),
            'activo':forms.TextInput(attrs={'class':'form-control'}),
        }

class pdaForm(forms.ModelForm):
    class Meta:
        model = pda
        fields = [
            'ot',
            'modelo_pda',
            'serie_pda',
            'fecha_ing',
            'fecha_desp',
            'serie_bateria',
            'num_inventario',
            'sucursal',
            'region',
            'estado',
            'dias_st',
            'descripcion_pda',
        ]

        labels = {
            'ot': 'Número de OT',
            'modelo_pda' : 'Modelo de PDA',
            'serie_pda' : 'Serie de PDA',
            'fecha_ing': 'Fecha de ingreso',
            'fecha_desp': 'Fecha de despacho',
            'serie_bateria': 'Serie de bateria',
            'num_inventario' : 'Número de inventario',
            'sucursal': 'Sucursal',
            'region': 'Región',
            'estado': 'Estado',
            'dias_st': 'Días en servicio técnico',
            'descripcion_pda': 'Descripción de la PDA',
        }

        widgets = {
            'ot' :forms.TextInput(attrs={'class':'form-control'}),
            'modelo_pda' :forms.TextInput(attrs={'class':'form-control'}),
            'serie_pda' :forms.TextInput(attrs={'class':'form-control'}),
            'fecha_ing':forms.DateInput(attrs={'class':'form-control'}),
            'fecha_desp':forms.DateInput(attrs={'class':'form-control'}),
            'serie_bateria':forms.TextInput(attrs={'class':'form-control'}),
            'num_inventario':forms.TextInput(attrs={'class':'form-control'}),
            'sucursal':forms.TextInput(attrs={'class':'form-control'}),
            'region':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.TextInput(attrs={'class':'form-control'}),
            'dias_st':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion_pda':forms.Textarea(attrs={'class':'form-control'}),  
        }

class telefonoForm(forms.ModelForm):
    class Meta:
        model = telefono
        fields =[
            'marca_tel',
            'modelo_tel',
            'serie_tel',
            'numero_tel',
            'fecha_ing_tel',
            'usuario_asig_tel',
            'departamento_usuario',
        ]

        labels = {
            'marca_tel': 'Marca del teléfono',
            'modelo_tel': 'Modelo del teléfono',
            'serie_tel' : 'Serie del teléfono',
            'numero_tel' : 'Número del teléfono',
            'fecha_ing_tel' : 'Fecha de ingreso del teléfono',
            'usuario_asig_tel' : 'Usuario asignado del teléfono',
            'departamento_usuario' : 'Departamento del usuario',
        }
        widgets = {
            'marca_tel' :forms.TextInput(attrs={'class':'form-control'}),
            'modelo_tel':forms.TextInput(attrs={'class':'form-control'}),
            'serie_tel':forms.TextInput(attrs={'class':'form-control'}),
            'numero_tel':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_ing_tel':forms.DateInput(attrs={'class':'form-control'}),
            'usuario_asig_tel':forms.TextInput(attrs={'class':'form-control'}),
            'departamento_usuario':forms.TextInput(attrs={'class':'form-control'}),
        }