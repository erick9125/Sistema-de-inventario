from apps.inventario.domain.entities import SESSION_EMAIL_KEY, SESSION_TTL_SECONDS, SESSION_UID_KEY
from apps.inventario.domain.exceptions import AuthNoConfigurado, CredencialesInvalidas
from apps.inventario.domain.ports.auth import AuthPort, AuthSession


class AuthService:
    def __init__(self, auth_port: AuthPort):
        self._auth_port = auth_port

    def login(self, email: str, password: str, session) -> AuthSession:
        auth_session = self._auth_port.authenticate(email, password)
        session[SESSION_UID_KEY] = auth_session.token
        session[SESSION_EMAIL_KEY] = auth_session.email
        session.set_expiry(SESSION_TTL_SECONDS)
        return auth_session

    def logout(self, session) -> None:
        session.flush()

    def is_authenticated(self, session) -> bool:
        return bool(session.get(SESSION_UID_KEY))

    def ensure_configured(self) -> None:
        if not self._auth_port.is_configured():
            raise AuthNoConfigurado(
                "Firebase no esta configurado. Define FIREBASE_API_KEY y el resto de variables en .env"
            )


__all__ = ["AuthService", "CredencialesInvalidas", "AuthNoConfigurado"]
