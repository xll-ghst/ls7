# Catalog API Backend

Готовый учебный Backend на Django REST Framework.

## Реализовано

- Django project + application
- Category и Product
- миграции
- serializers с валидацией и вычислением скидочной цены
- permissions
- каталог, фильтры, поиск и detail
- TOP товаров с cache.get/cache.set
- JWT authentication
- Swagger UI / OpenAPI
- Django admin

## Запуск Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Swagger:
http://127.0.0.1:8000/api/docs/

Schema:
http://127.0.0.1:8000/api/schema/

Admin:
http://127.0.0.1:8000/admin/

## Основные endpoints

POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/refresh/

GET /api/categories/
GET /api/products/
GET /api/products/{id}/
GET /api/products/top/

Фильтры:
GET /api/products/?category=1
GET /api/products/?min_price=100&max_price=1000
GET /api/products/?ordering=-price
GET /api/products/?search=чай

Для изменения/создания товаров требуется JWT и staff-права.
