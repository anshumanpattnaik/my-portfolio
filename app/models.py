from django.db import models


class TechPlatforms(models.Model):
    platform = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = True
        db_table = 'tech_platforms'


class TechStack(models.Model):
    domain_id = models.ManyToManyField(TechPlatforms)
    domain = models.CharField(max_length=100, blank=True)
    domain_url = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = True
        db_table = 'tech_stack'
