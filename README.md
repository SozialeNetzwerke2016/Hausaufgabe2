# Hausaufgabe1

Von:
Phillip Fiala,
Paul David Beck

# How to start the server:


Requirements:
Django 1.9.6 
Python 3.4


cd into Hausaufgabe2;
python3 manage.py runserver;


if you want to specify the port type:
python3 manage.py runserver 127.0.0.1:PORT/todoApp


type in browser: http://127.0.0.1:8000/todoApp
or http://127.0.0.1:PORT/todoApp for the specified port type


# Latest Changes
*06.05
Added Ineraction with Todos -> Add/Change/Delete 


*05.05.
Added Django Project: Hausaufgabe2
Added Django Application: todoApp
Copied templates from Hausaufgabe1
Changed css/js inlcudes: 
href: "css/bootstrap.min.css" => href: "{% static 'todoApp/css/bootstrap.min.css' %}"
----> Thats Djangos way looking up static files. In the header bevor any static file is called, we need {% load staticfiles %}. 

Changed Buttons:
href: "newTodo.html" => href: "{% url 'todoApp:newTodo' %}"

# Todo




