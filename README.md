# Project Management API 🚀

This is a RESTful API built with **Django** & **Django REST Framework**.  
It provides core project management features: user registration, authentication, project/task management, and comments — all secured with **JWT**.

---

## ✅ Features
- **User Registration & JWT Authentication**
- **CRUD for Users, Projects, Tasks, Comments**
- **Nested Routes**: Tasks nested under Projects, Comments nested under Tasks
- **Swagger API Docs** (`drf-yasg`)

---

## ⚙️ Setup

1️⃣ **Clone the repository**
```bash
git clone "https://github.com/Hassan25220/project_management_api_tool.git"

````

2️⃣ **Create & activate virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Run migrations**

```bash
python manage.py migrate
```

5️⃣ **Create superuser (optional)**

```bash
python manage.py createsuperuser
```

6️⃣ **Run the server**

```bash
python manage.py runserver
```

---

## 🔒 JWT Authentication

**Login to get tokens:**

```http
POST /api/users/login/
{
  "username": "your_username",
  "password": "your_password"
}
```

You’ll receive:

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

✅ **Use `access` token in Authorization header:**

```
Authorization: Bearer <your_access_token>
```

---

## 📚 API Docs (Swagger)

Swagger UI:

```
http://127.0.0.1:8000/api/swagger/
```

**How to use:**

1. Open the Swagger URL in your browser.
2. Click **`Authorize`** (🔒 button at top).
3. In the modal, paste your token:

   ```
   Bearer YOUR_ACCESS_TOKEN
   ```
4. Now you can try out any secured endpoints.

---

## 📌 Example Endpoints

* **Register**

  ```
  POST /api/users/register/
  ```

* **Projects**

  ```
  GET /api/projects/
  POST /api/projects/
  ```

* **Tasks (nested under project)**

  ```
  GET /api/projects/<project_id>/tasks/
  POST /api/projects/<project_id>/tasks/
  ```

* **Comments (nested under task)**

  ```
  GET /api/tasks/<task_id>/comments/
  POST /api/tasks/<task_id>/comments/
  ```

* **Update/Delete Comment**

  ```
  PATCH /api/comments/<comment_id>/
  DELETE /api/comments/<comment_id>/
  ```

---

## ✅ Swagger Security Settings

To enable **Authorize button**, make sure this is in `settings.py`:

```py
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
}
```

---

## 📌 Tech Stack

* Django
* Django REST Framework
* djangorestframework-simplejwt (JWT)
* drf-yasg (Swagger)

---

## ⚡ License

MIT — Use freely & build more 🚀

```

---

```
