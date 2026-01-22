from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

def home(request):
    return HttpResponse("Welcome to the Home Page")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)
    # return HttpResponse("Project Home Page")

def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    # task = Task.objects.get(id=id)
    return HttpResponse("Task to complete: %s" % task.title)

def hello(resquest, name):
    return HttpResponse("Hello, %s" % name)