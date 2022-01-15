from django.shortcuts import render

from app.core.clients.DBClient import DBClient


def index(request):
    with DBClient() as db_client:
        tech_platforms = db_client.fetch_tech_platforms().order_by('id')
        tech_skills = []
        for _index, platform in enumerate(tech_platforms, start=1):
            tech_stack = db_client.fetch_tech_stack_by_domain_id(_index)
            result = {
                "platform": platform.platform,
                "tech_stack": tech_stack
            }
            tech_skills.append(result)
        context = {
            "skills": tech_skills,
            "projects": db_client.fetch_projects(),
            "profile": db_client.fetch_profile()[0],
            "blogs": db_client.fetch_blogs()
        }
        return render(request, 'index.html', context)


def projects(request):
    with DBClient() as db_client:
        context = {
            "projects": db_client.fetch_projects(),
            "profile": db_client.fetch_profile()[0]
        }
        return render(request, 'projects.html', context)
