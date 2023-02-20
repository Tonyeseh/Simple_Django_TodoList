from django.shortcuts import render
from django.http import HttpResponse
from .models import Todolist, Item

# Create your views here.

def get_todo_by_id(response, id):
    Todo = Todolist.objects.get(id=id)
    return render(response, 'firstApp/todolist.html', {'todo': Todo})

def get_by_name(response, name):
    Todo = Todolist.objects.get(name=name)
    Todo_items = Todo.item_set.all()[0]
    return HttpResponse("<h1>{}</h1><br><p>{}</p>".format(Todo.name, str(Todo_items.text)))

def v1(response):
    return HttpResponse("<h1>Version 1!<h1>")

def home(response):
    return render(response, 'firstApp/home.html', {})
