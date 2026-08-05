class DomainError(Exception):
    """Error base del dominio."""


class CredencialesInvalidas(DomainError):
    """Email o contraseña incorrectos."""


class AuthNoConfigurado(DomainError):
    """Firebase u otro proveedor de auth no está configurado."""


class EntidadNoEncontrada(DomainError):
    """La entidad solicitada no existe."""
