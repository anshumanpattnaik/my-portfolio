from django.shortcuts import render

from app.models import TechPlatform, TechStack, Project

NAV_MENU = '<div class="nav-menu"><div class="label-container">' \
           '<a class="label">My Portfolio.</a></div>' \
           '<div class="menu-container">' \
           '<a href="#">Home</a>' \
           '<a href="#">Technical Skills</a>' \
           '<a href="#">Projects</a>' \
           '<a href="#">Blogs</a>' \
           '<a href="#">About Me</a>' \
           '<a href="#">Contacts</a>' \
           '</div>' \
           '</div>'


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
    context = {
        "skills": tech_skills,
        "projects": Project.objects.all(),
        "dom": NAV_MENU
    }
    return render(request, 'index.html', context)


def projects(request):
    # Projects
    context = {
        "projects": Project.objects.all(),
        "dom": NAV_MENU
    }
    return render(request, 'projects.html', context)
