from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_todo, name="Create ToDo"),
    path("<int:id>", views.get_todo_by_id, name="index"),
    path("<str:name>", views.get_by_name, name="Get Todo"),
    path("v1/", views.v1, name="Version 1"),
    path("", views.home, name="Home Page"),
]