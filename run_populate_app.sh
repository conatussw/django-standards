#!/bin/bash

docker compose exec web python manage.py migrate
#docker compose exec web echo "from users.models import User; User.objects.create_superuser('admin', 'admin@local.com', '123mudar!')" | python manage.py shell
echo "from users.models import User; User.objects.create_superuser('admin@local.com', '123mudar!')" | docker-compose exec -T web python manage.py shell
