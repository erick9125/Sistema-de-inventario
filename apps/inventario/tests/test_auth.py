import pytest

from apps.inventario.application.services.auth_service import AuthService
from apps.inventario.domain.entities import SESSION_EMAIL_KEY, SESSION_UID_KEY
from apps.inventario.domain.exceptions import AuthNoConfigurado, CredencialesInvalidas
from apps.inventario.domain.ports.auth import AuthSession


class FakeSession(dict):
    def __init__(self):
        super().__init__()
        self.expiry = None

    def set_expiry(self, value):
        self.expiry = value

    def flush(self):
        self.clear()
        self.expiry = None


class FakeAuthPort:
    def __init__(self, configured=True, fail=False):
        self.configured = configured
        self.fail = fail

    def is_configured(self):
        return self.configured

    def authenticate(self, email, password):
        if not self.configured:
            raise AuthNoConfigurado("no config")
        if self.fail:
            raise CredencialesInvalidas("bad creds")
        return AuthSession(token="token-123", email=email)


def test_auth_service_login_ok():
    service = AuthService(FakeAuthPort())
    session = FakeSession()
    result = service.login("a@b.com", "secret", session)
    assert result.token == "token-123"
    assert session[SESSION_UID_KEY] == "token-123"
    assert session[SESSION_EMAIL_KEY] == "a@b.com"
    assert session.expiry == 3600


def test_auth_service_login_invalid():
    service = AuthService(FakeAuthPort(fail=True))
    with pytest.raises(CredencialesInvalidas):
        service.login("a@b.com", "bad", FakeSession())


def test_auth_service_logout_clears_session():
    service = AuthService(FakeAuthPort())
    session = FakeSession()
    service.login("a@b.com", "secret", session)
    service.logout(session)
    assert SESSION_UID_KEY not in session
    assert not service.is_authenticated(session)


def test_auth_service_ensure_configured():
    service = AuthService(FakeAuthPort(configured=False))
    with pytest.raises(AuthNoConfigurado):
        service.ensure_configured()


def test_firebase_adapter_maps_errors(monkeypatch, settings):
    from apps.inventario.infrastructure.auth.firebase_adapter import FirebaseAuthAdapter

    settings.FIREBASE_CONFIG = {"apiKey": "x"}

    class FakeAuth:
        def sign_in_with_email_and_password(self, email, password):
            raise RuntimeError("boom")

    class FakeFirebase:
        def auth(self):
            return FakeAuth()

    monkeypatch.setattr(
        "apps.inventario.infrastructure.auth.firebase_adapter.pyrebase.initialize_app",
        lambda config: FakeFirebase(),
    )
    adapter = FirebaseAuthAdapter()
    with pytest.raises(CredencialesInvalidas):
        adapter.authenticate("a@b.com", "bad")


def test_firebase_adapter_success(monkeypatch, settings):
    from apps.inventario.infrastructure.auth.firebase_adapter import FirebaseAuthAdapter

    settings.FIREBASE_CONFIG = {"apiKey": "x"}

    class FakeAuth:
        def sign_in_with_email_and_password(self, email, password):
            return {"idToken": "abc"}

    class FakeFirebase:
        def auth(self):
            return FakeAuth()

    monkeypatch.setattr(
        "apps.inventario.infrastructure.auth.firebase_adapter.pyrebase.initialize_app",
        lambda config: FakeFirebase(),
    )
    session = FirebaseAuthAdapter().authenticate("a@b.com", "ok")
    assert session.token == "abc"
    assert session.email == "a@b.com"
