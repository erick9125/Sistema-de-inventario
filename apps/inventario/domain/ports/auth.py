from dataclasses import dataclass
from typing import Optional, Protocol, runtime_checkable


@dataclass(frozen=True)
class AuthSession:
    token: str
    email: str


@runtime_checkable
class AuthPort(Protocol):
    def authenticate(self, email: str, password: str) -> AuthSession:
        ...

    def is_configured(self) -> bool:
        ...
