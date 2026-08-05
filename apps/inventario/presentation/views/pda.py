from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from apps.inventario.application.services.reporte_service import ReporteService
from apps.inventario.infrastructure.persistence.models import Pda
from apps.inventario.presentation.filters import PdaFilter
from apps.inventario.presentation.forms import PdaForm
from apps.inventario.presentation.mixins import FirebaseLoginRequiredMixin, firebase_login_required


class PdaCreate(FirebaseLoginRequiredMixin, CreateView):
    model = Pda
    form_class = PdaForm
    template_name = "pda/pda_form.html"
    success_url = reverse_lazy("pda:pda_listar")


class PdaList(FirebaseLoginRequiredMixin, ListView):
    model = Pda
    template_name = "pda/pda_list.html"
    context_object_name = "pda_list"
    paginate_by = 20


class PdaUpdate(FirebaseLoginRequiredMixin, UpdateView):
    model = Pda
    form_class = PdaForm
    template_name = "pda/pda_form.html"
    success_url = reverse_lazy("pda:pda_listar")


class PdaDelete(FirebaseLoginRequiredMixin, DeleteView):
    model = Pda
    template_name = "pda/pda_delete.html"
    success_url = reverse_lazy("pda:pda_listar")


class PdaShow(FirebaseLoginRequiredMixin, DetailView):
    model = Pda
    template_name = "pda/pda_show.html"


@firebase_login_required
def pda_buscar(request):
    filtro = PdaFilter(request.GET, queryset=Pda.objects.all())
    return render(request, "pda/pda_search.html", {"filter": filtro})


class ReportePdaExcel(FirebaseLoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        return ReporteService().pdas()


pdaCreate = PdaCreate
pdaList = PdaList
pdaUpdate = PdaUpdate
pdaDelete = PdaDelete
pdaShow = PdaShow
pdaBuscar = pda_buscar
