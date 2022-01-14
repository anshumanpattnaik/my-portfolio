python3 manage.py collectstatic --no-input
python3 manage.py flush --no-input
python3 manage.py migrate
python3 manage.py makemigrations app
python3 manage.py migrate app
python3 admin.py