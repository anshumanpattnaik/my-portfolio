from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import TechPlatform, TechStack, Project, Profile, Blog


class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'thumbnail', 'link')


class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('full_name', 'photo', 'email', 'designation', 'about_me', 'copyright', 'github', 'twitter',
                    'linkedin', 'facebook', 'instagram')


class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('project_id', 'title', 'small_thumbnail', 'large_thumbnail', 'description', 'github_link',
                    'youtube_link', 'project_link', 'tech_stack', 'color_code')


class TechStackAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('domain', 'domain_url')


class TechPlatformAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['platform']


admin.site.register(TechPlatform, TechPlatformAdmin)
admin.site.register(TechStack, TechStackAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Blog, BlogAdmin)
