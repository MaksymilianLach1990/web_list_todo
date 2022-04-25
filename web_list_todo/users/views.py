from django.shortcuts import render

# Create your views here.

def registration(request):
    context = {}
    return render(request, 'todo/registration.html', context)

def login(request):
    context = {}
    return render(request, 'todo/login.html', context)

