from django.utils import timezone

from apps.inventario.domain.entities import SESSION_EMAIL_KEY


def shell_context(request):
    email = ""
    if hasattr(request, "session"):
        email = request.session.get(SESSION_EMAIL_KEY, "") or ""
    return {
        "usuario_sesion": email,
        "ahora": timezone.localtime(),
    }
