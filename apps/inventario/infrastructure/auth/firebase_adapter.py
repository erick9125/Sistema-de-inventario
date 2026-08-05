import pyrebase
from django.conf import settings

from apps.inventario.domain.exceptions import AuthNoConfigurado, CredencialesInvalidas
from apps.inventario.domain.ports.auth import AuthSession


class FirebaseAuthAdapter:
    def is_configured(self) -> bool:
        return bool(settings.FIREBASE_CONFIG.get("apiKey"))

    def authenticate(self, email: str, password: str) -> AuthSession:
        if not self.is_configured():
            raise AuthNoConfigurado(
                "Firebase no esta configurado. Define FIREBASE_API_KEY y el resto de variables en .env"
            )
        try:
            firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
            user = firebase.auth().sign_in_with_email_and_password(email, password)
        except AuthNoConfigurado:
            raise
        except Exception as exc:
            raise CredencialesInvalidas("Contraseña invalida, por favor intentelo nuevamente") from exc

        return AuthSession(token=str(user["idToken"]), email=email)
