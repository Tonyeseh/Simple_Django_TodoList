from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todolist, Item
from .forms import CreateListForm

# Create your views here.

def get_todo_by_id(response, id):
    Todo = Todolist.objects.get(id=id)
    return render(response, 'firstApp/todolist.html', {'todo': Todo})

def get_by_name(response, name):
    Todo = Todolist.objects.get(name=name)
    return render(response, 'firstApp/todolist.html', {'todo': Todo})

def v1(response):
    return HttpResponse("<h1>Version 1!<h1>")

def home(response):
    return render(response, 'firstApp/home.html', {})

def create_todo(response):
    if response.method == 'POST':
        form = CreateListForm(response.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            todo = Todolist(name=name)
            todo.save()
        return HttpResponseRedirect("/{}".format(todo.id))
    else:
        form = CreateListForm()
    return render(response, 'firstApp/create_todo.html', {"form": form})
