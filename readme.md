# Blog Project

A Django-powered blog application with user authentication, profile customization, and blog post management.

## Overview

This project is built using Django and includes two main apps:

- `blog` — blog content, views, templates, and static assets
- `user` — account signup, login, password reset, and profile management

The project is configured as a typical Django starter app with SQLite for local development, media uploads support, and static file handling for deployment.

## Project Structure

```text
blog_django_project/
├── blog/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── url.py
│   ├── views.py
│   └── tests.py
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── user/
│   ├── templates/
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── tests.py
├── media/
├── manage.py
├── requirements.txt
├── Procfile
├── build.sh
├── db.sqlite3
├── .gitignore
└── README.md
```

## Features

- User registration and login
- Password reset flow
- User profile page
- Profile image, banner, and bio management
- Blog pages and templates
- Media file support
- Deployment-friendly settings for Render/production hosting

## Requirements

- Python 3.10+
- Django 6.0.6
- Pip dependencies from `requirements.txt`

## Local Setup

1. Clone the repository
2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin access):

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

Then open the app in your browser at:

```text
http://127.0.0.1:8000/
```

## Environment Variables

The project supports optional environment variables for deployment and configuration:

- `SECRET_KEY` — Django secret key
- `DEBUG` — set to `True` or `False`
- `ALLOWED_HOSTS` — comma-separated allowed hosts
- `EMAIL_USER` — email username for password reset emails
- `EMAIL_PASSWORD` — email password or app password
- `TERMUX` — used for Android/Termux compatibility

## Deployment Notes

This repository includes deployment support files such as:

- `Procfile`
- `build.sh`
- WhiteNoise configuration in `blog_project/settings.py`

This makes it suitable for deployment to services like Render.

## Admin

To access the Django admin panel:

```text
http://127.0.0.1:8000/admin/
```

## License

This project does not include a license file. If you plan to share or distribute it publicly, consider adding an open-source license such as MIT.
