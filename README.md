
# 🍽️ LuxTable API - Sistema de Reservas para Restaurantes

Bienvenido a **LuxTable**, una API de arquitectura RESTful construida con **FastAPI** que permite a los restaurantes gestionar fácilmente las reservas de mesas. Esta API está diseñada para ser fácil de usar, segura y útil tanto para el restaurante como para los clientes.

---

## ✨ ¿Qué es LuxTable?

**LuxTable** es una herramienta que ayuda a los restaurantes a organizar sus reservas. Los clientes pueden reservar una mesa, y el restaurante puede ver, confirmar o cancelar esas reservas. También incluye funciones para:

- Crear y administrar usuarios, mesas y reservas.
- Iniciar sesión de forma segura con **tokens JWT**.
- Ver reportes sobre cuáles mesas o clientes tienen más reservas.
- Recibir notificaciones en tiempo real con **WebSockets**.
- Mantener los datos bien organizados y fáciles de entender.

---

## ⚙️ Características destacadas

- Crear, leer, actualizar y eliminar (CRUD) usuarios, mesas y reservas.
- Inicio de sesión seguro mediante tokenización
- Reportes fáciles para analizar reservas.
- Notificaciones en vivo cuando se hace o cancela una reserva.
- Manejo eficiente de errores para respuestas claras.
- Estructura lista para hacer pruebas automáticas del sistema.

---

## 🚀 ¿Cómo usar este proyecto?

### 1. Clonar el proyecto

```bash
git clone https://github.com/ADRIDEV2024/luxtable-api.git
cd luxetable-api
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables del entorno

Crea un archivo llamado **.env** con lo siguiente:

```env
DATABASE_URL=mysql:///./luxetable.db
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEBUG=True
```

### 5. Iniciar la aplicación

```bash
uvicorn app.main:app --reload
```

---
