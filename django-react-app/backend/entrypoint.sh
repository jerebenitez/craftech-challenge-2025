#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Uncomment below to flush db e.g. after running tests
# Just make sure you really mean it 
# python manage.py flush --no-input

# We have base custom user model so need to makemigrations out of box

python manage.py makemigrations core
python manage.py flush --no-input
python manage.py migrate
python manage.py loaddata initial_data.json
# python manage.py collectstatic --noinput

# Check if ENVIRONMENT is set to "PRODUCTION"
if [ "$ENVIRONMENT" = "PRODUCTION" ]; then
    echo "Running in PRODUCTION mode"
    exec gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3
else
    echo "Running in DEVELOPMENT mode"
    exec python manage.py runserver 0.0.0.0:8000
fi

exec "$@"
