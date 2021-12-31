from django.contrib.postgres.fields import ArrayField
from django.db import models


class TechPlatform(models.Model):
    platform = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = True
        db_table = 'tech_platforms'


class TechStack(models.Model):
    domain_id = models.ManyToManyField(TechPlatform)
    domain = models.CharField(max_length=100, blank=True)
    domain_url = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = True
        db_table = 'tech_stack'


class Project(models.Model):
    title = models.CharField(max_length=100, blank=True)
    thumbnail = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    github_link = models.CharField(max_length=100, blank=True)
    youtube_link = models.CharField(max_length=100, blank=True)
    project_link = models.CharField(max_length=100, blank=True)
    tech_stack = ArrayField(models.CharField(max_length=100), blank=True)
    color_code = models.CharField(max_length=100, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'projects'
        ordering = ['-published_date']


class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    about_me = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'profile'
