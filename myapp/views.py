from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page")

def projects(request):
    return HttpResponse("Project Home Page")

def tasks(request):
    return HttpResponse("Tasks Home Page")

def hello(resquest, name):
    return HttpResponse("Hello, %s", name)