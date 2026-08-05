from apps.inventario.application.services.auth_service import AuthService
from apps.inventario.infrastructure.auth.firebase_adapter import FirebaseAuthAdapter


def get_auth_service() -> AuthService:
    return AuthService(FirebaseAuthAdapter())
