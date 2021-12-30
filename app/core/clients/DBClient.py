from app.models import TechPlatform, TechStack, Project


class DBClient:

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @staticmethod
    def fetch_tech_platforms():
        return TechPlatform.objects.all()

    @staticmethod
    def fetch_tech_stack_by_domain_id(domain_id):
        return TechStack.objects.filter(domain_id=domain_id)

    @staticmethod
    def fetch_projects():
        return Project.objects.all()
