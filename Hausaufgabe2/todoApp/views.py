from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Todo;

# Create your views here.

def index(request):
    todos = Todo.objects.all();
    #TODO: sort todos by Date
    template = loader.get_template('todoApp/index.html')
    print(len(todos))
    context = {
        'todos': todos,
    }
    return HttpResponse(template.render(context, request))

def newTodo(request):
    template = loader.get_template('todoApp/newTodo.html')
    context = {}
    return HttpResponse(template.render(context, request))

def editTodo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    template = loader.get_template('todoApp/editTodo.html')
    context = {
        'todo': todo,
    }
    return HttpResponse(template.render(context, request))

def impressum(request):
    template = loader.get_template('todoApp/impressum.html')
    context = {}
    return HttpResponse(template.render(context, request))
