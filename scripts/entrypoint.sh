#!/bin/sh
create-superuser () {
    local username="$1"
    local email="$2"
    local password="$3"
    cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="$username").exists():
    User.objects.create_superuser("$username", "$email", "$password")
else:
    print('User "{}" exists already, not created'.format("$username"))
EOF
}

# Start nginx (Alpine uses openrc)
nginx

# Run migrations
cd /app
python manage.py migrate

create-superuser ${USERNAME:-admin} ${EMAIL:-admin@admin.de} ${PASSWORD:-changeme}
django-admin compilemessages > /dev/null 2>&1
echo 'Starting application'
#TODO: Increase worker amount. Currently bugged with scraper thread. Scraper threading needs to be fixed first
gunicorn --bind :6734 --workers 1 --preload main.wsgi
