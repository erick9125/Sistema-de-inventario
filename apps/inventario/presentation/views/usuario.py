from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from apps.inventario.infrastructure.persistence.models import Usuario
from apps.inventario.presentation.forms import UsuarioForm
from apps.inventario.presentation.mixins import FirebaseLoginRequiredMixin, InventarioSuccessMixin


class UsuarioCreate(InventarioSuccessMixin, CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuario/Usuario_form.html"
    success_url = reverse_lazy("usuario:usuario_listar")
    success_message = "Usuario registrado correctamente"


class UsuarioList(FirebaseLoginRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/usuario_list.html"
    context_object_name = "usuario_list"
    paginate_by = 10


class UsuarioUpdate(InventarioSuccessMixin, UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuario/Usuario_form.html"
    success_url = reverse_lazy("usuario:usuario_listar")
    success_message = "Usuario actualizado correctamente"


class UsuarioDelete(InventarioSuccessMixin, DeleteView):
    model = Usuario
    template_name = "usuario/usuario_delete.html"
    success_url = reverse_lazy("usuario:usuario_listar")
    success_message = "Usuario eliminado correctamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class UsuarioShow(FirebaseLoginRequiredMixin, DetailView):
    model = Usuario
    template_name = "usuario/usuario_show.html"


usuarioDelete = UsuarioDelete
usuarioShow = UsuarioShow
