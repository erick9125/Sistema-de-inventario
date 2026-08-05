from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from apps.inventario.application.services.reporte_service import ReporteService
from apps.inventario.infrastructure.persistence.models import Asignacion
from apps.inventario.presentation.filters import AsignacionFilter
from apps.inventario.presentation.forms import AsignacionForm
from apps.inventario.presentation.mixins import FirebaseLoginRequiredMixin, firebase_login_required


class AsignacionCreate(FirebaseLoginRequiredMixin, CreateView):
    model = Asignacion
    form_class = AsignacionForm
    template_name = "asignacion/asignacion_form.html"
    success_url = reverse_lazy("Asignacion:asignacion_listar")


class AsignacionList(FirebaseLoginRequiredMixin, ListView):
    model = Asignacion
    template_name = "asignacion/asignacion_list.html"
    context_object_name = "asignacion_list"
    paginate_by = 15


class AsignacionUpdate(FirebaseLoginRequiredMixin, UpdateView):
    model = Asignacion
    form_class = AsignacionForm
    template_name = "asignacion/asignacion_form.html"
    success_url = reverse_lazy("Asignacion:asignacion_listar")


class AsignacionDelete(FirebaseLoginRequiredMixin, DeleteView):
    model = Asignacion
    template_name = "asignacion/asignacion_delete.html"
    success_url = reverse_lazy("Asignacion:asignacion_listar")


class AsignacionShow(FirebaseLoginRequiredMixin, DetailView):
    model = Asignacion
    template_name = "asignacion/asignacion_show.html"


@firebase_login_required
def asignacion_buscar(request):
    filtro = AsignacionFilter(request.GET, queryset=Asignacion.objects.all())
    return render(request, "asignacion/asignacion_search.html", {"filter": filtro})


class ReporteAsignacionExcel(FirebaseLoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        return ReporteService().asignaciones()


asignacionList = AsignacionList
asignacionUpdate = AsignacionUpdate
asignacionDelete = AsignacionDelete
asignacionShow = AsignacionShow
asignacionBuscar = asignacion_buscar
