from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def projects (request):
    projects=list(Project.objects.values())
    return JsonResponse(projects,safe=False)
def tasks (request,title):
    task=Task.objects.get(title=title)
    return HttpResponse('tasks: %s' %task.title)
