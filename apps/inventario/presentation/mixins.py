from functools import wraps

from django.shortcuts import redirect

from apps.inventario.application.container import get_auth_service


def firebase_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not get_auth_service().is_authenticated(request.session):
            return redirect("/")
        return view_func(request, *args, **kwargs)

    return wrapper


class FirebaseLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not get_auth_service().is_authenticated(request.session):
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)
