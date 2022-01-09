import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
django.setup()

User = get_user_model()
User.objects.create_superuser(os.environ.get('DATABASE_USER'), os.environ.get('ADMIN_EMAIL'),
                              os.environ.get('DATABASE_PASSWORD'))
