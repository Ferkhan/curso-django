from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('hello/<str:name>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('about/', views.about),
    path('create_task/', views.create_task)
]