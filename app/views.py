from django.shortcuts import render

from app.models import TechPlatform, TechStack, Project


def index(request):

    # Technical Skills
    tech_platforms = TechPlatform.objects.all()
    tech_skills = []
    for _index, platform in enumerate(tech_platforms, start=1):
        tech_stack = TechStack.objects.filter(domain_id=_index)
        result = {
            "platform": platform.platform,
            "tech_stack": tech_stack
        }
        tech_skills.append(result)

    # Projects
    projects = Project.objects.all()
    context = {
        "skills": tech_skills,
        "projects": projects
    }
    return render(request, 'index.html', context)
