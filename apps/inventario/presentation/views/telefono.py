from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from apps.inventario.application.services.reporte_service import ReporteService
from apps.inventario.infrastructure.persistence.models import Telefono
from apps.inventario.presentation.filters import TelefonoFilter
from apps.inventario.presentation.forms import TelefonoForm
from apps.inventario.presentation.mixins import FirebaseLoginRequiredMixin, firebase_login_required


class TelefonoCreate(FirebaseLoginRequiredMixin, CreateView):
    model = Telefono
    form_class = TelefonoForm
    template_name = "telefono/telefono_form.html"
    success_url = reverse_lazy("telefono:telefono_listar")


class TelefonoList(FirebaseLoginRequiredMixin, ListView):
    model = Telefono
    template_name = "telefono/telefono_list.html"
    context_object_name = "telefono_list"
    paginate_by = 10


class TelefonoUpdate(FirebaseLoginRequiredMixin, UpdateView):
    model = Telefono
    form_class = TelefonoForm
    template_name = "telefono/telefono_form.html"
    success_url = reverse_lazy("telefono:telefono_listar")


class TelefonoDelete(FirebaseLoginRequiredMixin, DeleteView):
    model = Telefono
    template_name = "telefono/telefono_delete.html"
    success_url = reverse_lazy("telefono:telefono_listar")


class TelefonoShow(FirebaseLoginRequiredMixin, DetailView):
    model = Telefono
    template_name = "telefono/telefono_show.html"


@firebase_login_required
def telefono_buscar(request):
    filtro = TelefonoFilter(request.GET, queryset=Telefono.objects.all())
    return render(request, "telefono/telefono_search.html", {"filter": filtro})


class ReporteTelefonoExcel(FirebaseLoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        return ReporteService().telefonos()


telefonoCreate = TelefonoCreate
telegonoList = TelefonoList
telefonoUpdate = TelefonoUpdate
telefonoDelete = TelefonoDelete
telefonoShow = TelefonoShow
telefonoBuscar = telefono_buscar
