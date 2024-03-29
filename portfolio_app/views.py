from django.shortcuts import get_object_or_404, render

from .models import Project


# Эндпоинт главной страницы со всеми проектами
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


# Эндпоинт детальной страницы проекта
def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/detail.html', {'project_detail': project_detail})
