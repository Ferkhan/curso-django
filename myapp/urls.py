from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home),
    path('hello/<str:name>/', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
]