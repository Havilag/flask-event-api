# 📅 API de Gestión de Eventos y Reservas

¡Bienvenido! Esta es una **REST API** robusta y escalable desarrollada con **Flask** para la gestión y reserva de entradas a eventos. El sistema cuenta con arquitectura limpia, control de acceso basado en roles (RBAC), persistencia de datos en una base de datos relacional y validaciones de datos en capas de entrada.

---

## 🚀 Características Principales

- **Framework Flask:** Uso de `Flask-RESTful` para una organización limpia de recursos y endpoints.
- **Base de Datos PostgreSQL:** Persistencia de datos relacional gestionada mediante **SQLAlchemy ORM**.
- **Autenticación y Autorización Avanzada:**
  - Protección de rutas con tokens **JWT (JSON Web Tokens)** mediante `Flask-JWT-Extended`.
  - Control de acceso personalizado por roles (`@roles_required`) para restringir recursos según el tipo de usuario.
- **Seguridad de Datos:**
  - Contraseñas hasheadas utilizando **Bcrypt**.
  - Encriptación simétrica mediante **Fernet**.
- **Lógica de Negocio Avanzada:**
  - Control automático de stock de entradas durante la creación y cancelación de reservas.
- **Validaciones con Pydantic:**
  - Validación y sanitización estricta de datos JSON entrantes.
- **Documentación Interactiva:**
  - Integración de **Swagger UI** para pruebas y exploración de endpoints.

---

## 🛠️ Tecnologías y Librerías Utilizadas

- **Python 3.x**
- **Flask**
- **Flask-RESTful**
- **Flask-SQLAlchemy**
- **psycopg2-binary**
- **Flask-JWT-Extended**
- **Bcrypt**
- **Cryptography (Fernet)**
- **Pydantic**
- **Flask-Swagger-UI**
- **PostgreSQL**

---

## 📁 Estructura del Proyecto

El proyecto sigue una arquitectura limpia orientada al dominio y segmentada por responsabilidades.

```text
MODULO02/
│
├── app/
│   ├── __init__.py
│   ├── router.py
│   │
│   ├── models/
│   │   ├── booking_model.py
│   │   ├── category_model.py
│   │   ├── event_model.py
│   │   ├── role_model.py
│   │   └── user_model.py
│   │
│   ├── resources/
│   │   ├── auth_resource.py
│   │   ├── booking_resource.py
│   │   ├── category_resource.py
│   │   ├── event_resource.py
│   │   ├── role_resource.py
│   │   └── user_resource.py
│   │
│   ├── schemas/
│   │   ├── auth_schema.py
│   │   ├── booking_schema.py
│   │   ├── category_schema.py
│   │   ├── event_schema.py
│   │   ├── role_schema.py
│   │   └── user_schema.py
│   │
│   ├── services/
│   │   ├── booking_service.py
│   │   ├── category_service.py
│   │   ├── event_service.py
│   │   ├── role_service.py
│   │   └── user_service.py
│   │
│   ├── static/
│   │   └── swagger.json
│   │
│   └── utils/
│       └── security.py
│
├── entorno_virtual/
├── migrations/
├── .env
├── config.py
├── db.py
├── Diagram.png
├── key_generator.py
├── README.md
├── requirements.txt
└── run.py
```

---

## 📐 Modelo de Base de Datos (DER)

El sistema utiliza un diseño relacional optimizado para garantizar la integridad de los datos entre usuarios, roles, eventos, categorías y reservas.

### Diagrama Entidad-Relación

<p align="center">
  <img src="./Diagram.png" alt="Diagrama Entidad Relación" width="900">
</p>

---

## 🔐 Roles del Sistema

El sistema implementa un esquema de **Control de Acceso Basado en Roles (RBAC)**.

| ID | Rol | Descripción |
|----|------|-------------|
| `1` | Administrador | Acceso total al sistema y gestión completa de usuarios. |
| `2` | Personal / Trabajador | Gestión operativa y visualización de registros. |
| `3` | Público General | Registro, autenticación y gestión de sus propias reservas. |

---

## 🛣️ Endpoints Principales

### 🔑 Autenticación

| Endpoint | Método | Acceso | Descripción |
|-----------|---------|---------|-------------|
| `/api/v1/register` | `POST` | Público | Registra un usuario con rol Público (`3`). |
| `/api/v1/login` | `POST` | Público | Autentica credenciales y retorna un JWT válido. |

### 👥 Usuarios

| Endpoint | Método | Protección | Descripción |
|-----------|---------|------------|-------------|
| `/api/v1/users` | `GET` | `@jwt_required` + `@roles_required(1,2)` | Lista todos los usuarios registrados. |
| `/api/v1/users` | `POST` | `@jwt_required` + `@roles_required(1)` | Crea usuarios de cualquier rol. |
| `/api/v1/users/<int:user_id>` | `GET` | `@jwt_required` | Obtiene un usuario por ID. |
| `/api/v1/users/<int:user_id>` | `PUT` | `@jwt_required` | Actualiza un usuario existente. |
| `/api/v1/users/<int:user_id>` | `DELETE` | `@jwt_required` | Elimina un usuario. |

### 🎟️ Reservas

| Endpoint | Método | Protección | Descripción |
|-----------|---------|------------|-------------|
| `/api/v1/bookings` | `POST` | `@jwt_required` | Valida disponibilidad y genera una reserva descontando stock automáticamente. |
| `/api/v1/bookings/<int:booking_id>` | `DELETE` | `@jwt_required` | Cancela la reserva y devuelve los tickets al stock del evento. |

---

## 💼 Lógica de Negocio Implementada

### Creación de Reservas

Al registrar una reserva:

1. Se valida que el evento exista.
2. Se verifica la disponibilidad de entradas.
3. Se crea la reserva.
4. Se descuenta automáticamente el stock disponible.

### Cancelación de Reservas

Al cancelar una reserva:

1. Se actualiza el estado a `cancelled`.
2. Se restauran los tickets reservados al stock del evento.
3. Se mantiene la trazabilidad histórica de la operación.

---

## 📦 Instalación y Configuración Local

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2️⃣ Crear y activar entorno virtual

#### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
FLASK_APP=app.py
FLASK_ENV=development

DATABASE_URL=postgresql://postgres:tu_contraseña@localhost:5432/tu_base_de_datos

JWT_SECRET_KEY=tu_clave_secreta_jwt_super_segura
FERNET_SECRET_KEY=tu_clave_fernet_generada
```

### 5️⃣ Crear la base de datos

```sql
CREATE DATABASE events_db;
```

### 6️⃣ Ejecutar migraciones

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 7️⃣ Ejecutar la aplicación

```bash
python run.py
```

o

```bash
flask run
```

---

## 📚 Documentación Swagger

Una vez iniciada la aplicación, la documentación interactiva estará disponible en:

```text
http://localhost:5000/swagger
```

Desde Swagger podrás:

- Visualizar todos los endpoints.
- Probar peticiones directamente desde el navegador.
- Consultar esquemas de entrada y salida.
- Revisar códigos de respuesta HTTP.

---

## 🔒 Seguridad Implementada

- Autenticación mediante JWT.
- Protección de rutas sensibles.
- Control de acceso basado en roles (RBAC).
- Contraseñas almacenadas con hash Bcrypt.
- Cifrado de información sensible mediante Fernet.
- Validación de datos con Pydantic.

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica de Backend con:

- Flask
- PostgreSQL
- SQLAlchemy
- JWT
- Pydantic
- Swagger UI

---