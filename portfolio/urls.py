import os

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(os.environ.get('ADMIN_INTERNAL_URL'), admin.site.urls),
    path('', include('app.urls'))
]
