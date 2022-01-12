#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
  while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
    sleep 0.1
  done
fi

python3 manage.py collectstatic
python3 manage.py flush --no-input
python3 manage.py migrate
python3 manage.py makemigrations app
python3 manage.py migrate app
python3 admin.py

exec "$@"