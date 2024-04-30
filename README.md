# Conatus Standards

This project is used by Conatus Software as reference for develop Django based applications.
It contains valuable information about tools and practices to developing single page websites,
REST APIs and Full Stack Web Applications.

## Running the project

The project is configured with Docker, so, all you need is to run:

```bash
# If is the first time the compose will build the images for the services
docker compose up -d
# Run migrations
docker compose exec web python manage.py migrate

# That's all. It's done!
```

## Stack

- Django 5
- Django Database URL
- Model Bakery
- Django Widget Tweaks
- Django Storages
- Gunicorn
- Django Sass
- Django Stubs
- PyTest
- ruff
- MkDocs
- MkDocs material
