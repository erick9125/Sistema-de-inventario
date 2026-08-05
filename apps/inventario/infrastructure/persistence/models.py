from django.db import models
from django.utils import timezone


class Equipo(models.Model):
    id = models.IntegerField(primary_key=True)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    serie = models.CharField(max_length=250)
    rotulo = models.IntegerField(default=0)
    fecha_ing = models.DateTimeField(default=timezone.now)
    tipo = models.CharField(max_length=100)
    activo = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=600)

    class Meta:
        app_label = "inventario"
        db_table = "inventario_equipo"
        ordering = ["id"]
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    def __str__(self):
        return f"{self.marca} {self.modelo}"


class Asignacion(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario_asig = models.CharField(max_length=350)
    cargo = models.CharField(max_length=150)
    departamento = models.CharField(max_length=300)
    fecha_entrega = models.DateTimeField(default=timezone.now)
    marca_equipo_asig = models.CharField(max_length=200)
    modelo_equipo_asig = models.CharField(max_length=200)
    serie_equipo_asig = models.CharField(max_length=250)
    rotulo_equipo_asig = models.IntegerField(default=0)
    tipo_equipo = models.CharField(max_length=100)
    activo = models.BooleanField(default=False)

    class Meta:
        app_label = "inventario"
        db_table = "inventario_asignacion"
        verbose_name = "Asignacion"
        verbose_name_plural = "Asignaciones"

    def __str__(self):
        return self.usuario_asig


class Telefono(models.Model):
    id = models.IntegerField(primary_key=True)
    marca_tel = models.CharField(max_length=200)
    modelo_tel = models.CharField(max_length=200)
    serie_tel = models.CharField(max_length=250)
    numero_tel = models.IntegerField(default=0)
    fecha_ing_tel = models.DateTimeField(default=timezone.now)
    usuario_asig_tel = models.CharField(max_length=200)
    departamento_usuario = models.CharField(max_length=250)

    class Meta:
        app_label = "inventario"
        db_table = "inventario_telefono"
        verbose_name = "Telefono"
        verbose_name_plural = "Telefonos"

    def __str__(self):
        return str(self.numero_tel)


class Pda(models.Model):
    id = models.IntegerField(primary_key=True)
    ot = models.CharField(max_length=200)
    modelo_pda = models.CharField(max_length=350)
    serie_pda = models.CharField(max_length=250)
    fecha_ing = models.DateTimeField(default=timezone.now)
    fecha_desp = models.DateTimeField(default=timezone.now)
    serie_bateria = models.CharField(max_length=250)
    num_inventario = models.CharField(max_length=250)
    sucursal = models.CharField(max_length=200)
    region = models.CharField(max_length=250)
    estado = models.CharField(max_length=100)
    dias_st = models.IntegerField(default=0)
    descripcion_pda = models.CharField(max_length=250)

    class Meta:
        app_label = "inventario"
        db_table = "inventario_pda"
        verbose_name = "PDA"
        verbose_name_plural = "PDAs"

    def __str__(self):
        return self.serie_pda


class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    email = models.CharField(max_length=30, null=True, blank=True)
    clave = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        app_label = "inventario"
        db_table = "inventario_usuario"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Compatibilidad con imports legados
equipo = Equipo
asignacion = Asignacion
telefono = Telefono
pda = Pda
usuario = Usuario
