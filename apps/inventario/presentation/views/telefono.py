from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from apps.inventario.application.services.reporte_service import ReporteService
from apps.inventario.infrastructure.persistence.models import Telefono
from apps.inventario.presentation.filters import TelefonoFilter
from apps.inventario.presentation.forms import TelefonoForm
from apps.inventario.presentation.mixins import (
    FirebaseLoginRequiredMixin,
    InventarioSuccessMixin,
    firebase_login_required,
)


class TelefonoCreate(InventarioSuccessMixin, CreateView):
    model = Telefono
    form_class = TelefonoForm
    template_name = "telefono/telefono_form.html"
    success_url = reverse_lazy("telefono:telefono_listar")
    success_message = "Telefono registrado correctamente"


class TelefonoList(FirebaseLoginRequiredMixin, ListView):
    model = Telefono
    template_name = "telefono/telefono_list.html"
    context_object_name = "telefono_list"
    paginate_by = 10


class TelefonoUpdate(InventarioSuccessMixin, UpdateView):
    model = Telefono
    form_class = TelefonoForm
    template_name = "telefono/telefono_form.html"
    success_url = reverse_lazy("telefono:telefono_listar")
    success_message = "Telefono actualizado correctamente"


class TelefonoDelete(InventarioSuccessMixin, DeleteView):
    model = Telefono
    template_name = "telefono/telefono_delete.html"
    success_url = reverse_lazy("telefono:telefono_listar")
    success_message = "Telefono eliminado correctamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class TelefonoShow(FirebaseLoginRequiredMixin, DetailView):
    model = Telefono
    template_name = "telefono/telefono_show.html"


@firebase_login_required
def telefono_buscar(request):
    filtro = TelefonoFilter(request.GET, queryset=Telefono.objects.all())
    return render(
        request,
        "telefono/telefono_search.html",
        {"filter": filtro, "object_list": filtro.qs},
    )


class ReporteTelefonoExcel(FirebaseLoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        return ReporteService().telefonos()


telefonoCreate = TelefonoCreate
telegonoList = TelefonoList
telefonoUpdate = TelefonoUpdate
telefonoDelete = TelefonoDelete
telefonoShow = TelefonoShow
telefonoBuscar = telefono_buscar
