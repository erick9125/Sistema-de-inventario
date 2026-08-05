from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from apps.inventario.application.services.reporte_service import ReporteService
from apps.inventario.infrastructure.persistence.models import Equipo
from apps.inventario.presentation.filters import EquipoFilter
from apps.inventario.presentation.forms import EquipoForm
from apps.inventario.presentation.mixins import (
    FirebaseLoginRequiredMixin,
    InventarioSuccessMixin,
    firebase_login_required,
)


class EquipamientoCreate(InventarioSuccessMixin, CreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = "equipos/equipo_form.html"
    success_url = reverse_lazy("equipos:equipo_listar")
    success_message = "Equipo registrado correctamente"


class EquipoList(FirebaseLoginRequiredMixin, ListView):
    model = Equipo
    template_name = "equipos/equipo_list.html"
    context_object_name = "equipo_list"
    paginate_by = 20


class EquipoUpdate(InventarioSuccessMixin, UpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = "equipos/equipo_form.html"
    success_url = reverse_lazy("equipos:equipo_listar")
    success_message = "Equipo actualizado correctamente"


class EquipoDelete(InventarioSuccessMixin, DeleteView):
    model = Equipo
    template_name = "equipos/equipo_delete.html"
    success_url = reverse_lazy("equipos:equipo_listar")
    success_message = "Equipo eliminado correctamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class EquipoShow(FirebaseLoginRequiredMixin, DetailView):
    model = Equipo
    template_name = "equipos/equipo_show.html"


@firebase_login_required
def equipo_buscar(request):
    filtro = EquipoFilter(request.GET, queryset=Equipo.objects.all())
    return render(request, "equipos/equipo_search.html", {"filter": filtro, "object_list": filtro.qs})


class ReporteEquipoExcel(FirebaseLoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        return ReporteService().equipos()


equipoList = EquipoList
equipoUpdate = EquipoUpdate
equipoDelete = EquipoDelete
equipoShow = EquipoShow
equipoBuscar = equipo_buscar
