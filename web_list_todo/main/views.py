from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login

# Create your views here.

def home(request):
    context = {}
    return render(request, 'main/homePage.html', context)

def sing_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sing_up.html', {"form": form})