from django.contrib import admin
from .models import TechPlatform, TechStack, Project, Profile, Blog

admin.site.register(TechPlatform)
admin.site.register(TechStack)
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Blog)
