from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Todo
import operator
import string
import sys
from datetime import datetime
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    template = loader.get_template('todoApp/index.html')
    context = {
        'todos': todos,
    }
    for todo in todos:
        print(todo.date.hour)
    return HttpResponse(template.render(context, request))

def newTodo(request):
    template = loader.get_template('todoApp/newTodo.html')
    context = {}
    return HttpResponse(template.render(context, request))

def addTodo(request):
    #werte die Eingaben aus
    try:
        name = request.POST['Name']
        date = request.POST['Date'].split(sep="/")
        time = request.POST['Time'].split(sep=":")
        #TODO: Test if input is Valid
        process = request.POST['Process']
        print(int(float(date[2])),int(float(date[1])),int(float(date[0])),int(float(time[0])),int(float(time[1])))

        todo = Todo(name=name,date=datetime(int(float(date[2])),int(float(date[1])),int(float(date[0])),int(float(time[0]))%24,int(float(time[1]))), process=process )
        todo.save()

    except:
        print("Something fucks up with Input")

    return redirect('todoApp:index')

def editTodo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
    except:
        print("No Todo with id: "+todo_id+" available")
    template = loader.get_template('todoApp/editTodo.html')
    context = {
        'todo': todo,
    }
    return HttpResponse(template.render(context, request))

def changeTodo(request, todo_id):
     #werte die Eingaben aus
    try:
        todo = Todo.objects.get(id=todo_id)
        print(todo_id)
        name = request.POST['Name']
        print(name)
        date = request.POST['Date'].split(sep="/")
        print(date)
        time = request.POST['Time'].split(sep=":")
        print(time)
        #TODO: Test if input is Valid
        process = request.POST['Process']


        print(int(float(date[2])),int(float(date[1])),int(float(date[0])),int(float(time[0])),int(float(time[1])))
        todo.name = name
        todo.date = datetime(int(float(date[2])),int(float(date[1])),int(float(date[0])),int(float(time[0]))%24,int(float(time[1])))
        todo.process = process

        todo.save()

    except:
        print("Something fucks up with Input")

    return redirect('todoApp:index')

def impressum(request):
    template = loader.get_template('todoApp/impressum.html')
    context = {}
    return HttpResponse(template.render(context, request))

def deleteTodo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id);
        todo.delete()
    except:
        print("Something went wrong")

    return redirect('todoApp:index')
