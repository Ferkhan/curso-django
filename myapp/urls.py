from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('hello/<str:name>', views.hello),
    path('projects/', views.projects),
    path('tasks/<int:id>', views.tasks),
    path('about/', views.about)
]