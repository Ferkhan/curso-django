from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Project, Task
from .forms import CreateTaskForm

def home(request):
    title = "Primera app con Django"
    return render(request, 'index.html', {
        'title': title
    })
    # return HttpResponse("Welcome to the Home Page")

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html', {
        'projects': projects
    })
    # return JsonResponse(projects, safe=False)
    # return HttpResponse("Project Home Page")

def tasks(request):
    # task = get_object_or_404(Task, id=id)
    # task = Task.objects.get(id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })
    # return HttpResponse("Task to complete: %s" % task.title)

def hello(resquest, name):
    return HttpResponse("Hello, %s" % name)

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("About Page")

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': CreateTaskForm()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect("/myapp/tasks/")