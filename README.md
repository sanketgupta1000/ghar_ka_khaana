# Ghar Ka Khaana

>A simple Django-based food ordering platform (learning/demo project).

## Overview

Ghar Ka Khaana is a Django web application that implements a basic food-ordering workflow. It includes the following apps:

- `deliveryman` — delivery personnel models and views
- `foodie` — customer-facing views, auth and menus
- `kitchen` — kitchen staff views and order processing
- `order` — order models and business logic
- `user` — custom user model (`user.Account`)

The project was created with Django 5.0.1 and uses SQLite as the default database.

## Requirements

- Python 3.8+ (3.11+ recommended)
- pip
- Virtualenv (recommended)
- Django 5.0.1
- `django-bootstrap5` (used in templates)

There is no `requirements.txt` in the repo; install the basics manually as shown below.

## Quick start (development)

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install "Django==5.0.1" django-bootstrap5
```

3. Run migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Database

The project uses SQLite by default — the database file is `db.sqlite3` in the project root.

## Configuration notes

- The Django settings file is `ghar_ka_khaana/settings.py` and currently sets `DEBUG = True` and includes a hard-coded `SECRET_KEY`. Do not use this configuration in production.
- `AUTH_USER_MODEL` is set to `user.Account`.
- Static files are served from the `static/` directory during development (see `STATICFILES_DIRS` in settings).

## Running tests

```bash
python manage.py test
```

## Useful files

- `manage.py` — Django management entrypoint
- `ghar_ka_khaana/settings.py` — project settings
- `templates/` — HTML templates
- `static/` — CSS, JS and image assets

## Contributing

This appears to be a demo/learning project. If you plan to extend it:

- Add a `requirements.txt` or `pyproject.toml` to pin dependencies.
- Remove hard-coded secret keys and configure environment-based settings.
- Add documentation for app-specific behaviour and API endpoints.

## License

No license specified. Add a LICENSE file if you wish to set one.
