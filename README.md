# Sistema de Inventario

Aplicacion web para gestionar inventario de equipos, asignaciones, PDA, telefonos y usuarios.

Stack: **Django 5.2**, SQLite, **Bootstrap 5** (toasts), autenticacion con **Firebase Auth** (puerto/adaptador), despliegue con **Docker**.

Rama UI: `mejora/redisenio-ui-bootstrap`

---

## Requisitos

- Python 3.11+ (recomendado 3.12; en Windows usar `py`)
- Cuenta Firebase con Authentication (Email/Password)
- Docker Desktop (opcional)

---

## Inicio rapido (local)

```bash
cd "C:\Users\Equipo\Documents\Proyectos Senior\Sistema-de-inventario"
py -3.12 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Edita `.env` con `SECRET_KEY` y variables `FIREBASE_*`.

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abre http://127.0.0.1:8000/ e inicia sesion con un usuario de Firebase.

---

## Docker

```bash
copy .env.example .env
```

En `.env` para Docker usa `SQLITE_PATH=/app/data/db.sqlite3` (o deja que `docker-compose` lo defina).

```bash
docker compose up --build
```

App en http://localhost:8000/

```bash
docker compose logs -f web
docker compose down
```

---

## Tests

```bash
pytest
```

Cubre autenticacion (AuthService + adapter mock), CRUD de servicios, reportes Excel y proteccion de vistas sin sesion.

---

## Arquitectura (Clean Architecture - opcion A)

```text
apps/inventario/
  domain/            # reglas, excepciones, puertos (AuthPort, repositorios)
  application/       # servicios / casos de uso + container DI
  infrastructure/    # Firebase, ORM Django, exportador Excel
  presentation/      # views, forms, filters, urls, mixins
  migrations/
```

Flujo de autenticacion:

1. `presentation` recibe POST de login
2. `AuthService` orquesta la sesion Django
3. `FirebaseAuthAdapter` implementa `AuthPort` (unico lugar con Pyrebase)
4. Errores se traducen a `CredencialesInvalidas` / `AuthNoConfigurado`

Principios aplicados:

- **S** servicios por agregado (Equipo, Usuario, etc.)
- **O/D** auth y reportes detras de puertos/adaptadores
- **I** repositorios pequenos por entidad
- Vistas delgadas; Excel centralizado en `ExcelExporter`

---

## Variables de entorno

Copia `.env.example` a `.env`. Nunca subas `.env`.

| Variable | Descripcion |
|----------|-------------|
| `SECRET_KEY` | Clave secreta Django |
| `DEBUG` | `True` desarrollo / `False` produccion |
| `ALLOWED_HOSTS` | Hosts separados por coma |
| `FIREBASE_API_KEY` | API key Firebase |
| `FIREBASE_AUTH_DOMAIN` | Dominio auth |
| `FIREBASE_DATABASE_URL` | URL Realtime Database |
| `FIREBASE_PROJECT_ID` | ID proyecto |
| `FIREBASE_STORAGE_BUCKET` | Bucket |
| `FIREBASE_MESSAGING_SENDER_ID` | Sender ID |
| `SQLITE_PATH` | Ruta SQLite |
| `SECURE_SSL_REDIRECT` | HTTPS redirect (prod) |
| `SESSION_COOKIE_SECURE` | Cookie sesion HTTPS |
| `CSRF_COOKIE_SECURE` | Cookie CSRF HTTPS |

---

## Seguridad

- Secretos solo en `.env`
- CRUD e informes requieren sesion Firebase
- Logout hace `session.flush`
- Login solo `POST` + CSRF
- Headers XSS / clickjacking / nosniff / SameSite
- Contraseña de usuarios de inventario hasheada (`PasswordInput`)
- Token Firebase no se imprime en consola

Recomendado: rotar API key Firebase y `SECRET_KEY` si estuvieron publicas en el historial del repo.

---

## Modulos

| Modulo | Funcion |
|--------|---------|
| Usuarios | Personas del inventario |
| Equipos | Hardware |
| Asignaciones | Entrega de equipos |
| PDA | Dispositivos / ST |
| Telefonos | Lineas y terminales |
| Informes | Exportacion Excel |

---

## Convencion de commits (español)

```text
chore: crear base Docker y variables de entorno
refactor: aplicar arquitectura limpia por capas
feat: integrar Firebase detras de puerto y adaptador
test: agregar cobertura de auth y servicios
fix: endurecer sesiones y formularios
```

---

## Admin Django

```bash
python manage.py createsuperuser
```

Disponible en `/admin/` (independiente de Firebase).

---

## Licencia

[Unlicense](LICENSE)
