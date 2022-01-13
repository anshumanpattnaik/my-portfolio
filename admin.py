import json
import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
django.setup()

from app.models import Blog, Profile, Project, TechPlatform, TechStack

User = get_user_model()
User.objects.create_superuser(os.environ.get('DATABASE_USER'), os.environ.get('ADMIN_EMAIL'),
                              os.environ.get('DATABASE_PASSWORD'))

# Delete all records
Blog.objects.all().delete()
Profile.objects.all().delete()
Project.objects.all().delete()
TechPlatform.objects.all().delete()
TechStack.objects.all().delete()

# Blogs Data
blogs = json.load(open('database/Blog.json'))
for blog in blogs:
    b = Blog(title=blog['title'], thumbnail=blog['thumbnail'], link=blog['link'])
    b.save()

# Profile Data
profile_results = json.load(open('database/Profile.json'))
profile = profile_results[0]
Profile(full_name=profile['full_name'], photo=profile['photo'], email=profile['email'],
        designation=profile['designation'], about_me=profile['about_me'], copyright=profile['copyright'],
        github=profile['github'], twitter=profile['twitter'], linkedin=profile['linkedin'],
        facebook=profile['facebook'], instagram=profile['instagram']).save()

# Project Data
projects = json.load(open('database/Projects.json'))
for project in projects:
    Project(project_id=project['project_id'], title=project['title'], small_thumbnail=project['small_thumbnail'],
            large_thumbnail=project['large_thumbnail'], description=project['description'],
            github_link=project['github_link'], youtube_link=project['youtube_link'],
            project_link=project['project_link'], tech_stack=project['tech_stack'],
            color_code=project['color_code']).save()

# TechPlatform / TechStack
tech_platforms = json.load(open('database/TechPlatform.json'))
tech_stacks = json.load(open('database/TechStack.json'))

for tech_platform in tech_platforms:
    t = TechPlatform.objects.create(platform=tech_platform['platform'])
    for tech_stack in tech_stacks:
        if tech_stack['platform_id'] == tech_platform['platform_id']:
            tech = TechStack.objects.create(domain=tech_stack['domain'], domain_url=tech_stack['domain_url'])
            tech.domain_id.add(t)
