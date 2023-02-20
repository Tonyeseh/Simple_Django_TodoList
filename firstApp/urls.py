from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("<str:name>", views.get_by_name, name="Get Todo"),
    path("v1/", views.v1, name="Version 1"),
]