from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import Game

# Create your views here.
def index(request):
    games = Game.objects.all()
    context = {
        'games':games,
        'title':"Zteam"
    }
    return render(request, 'store/index.html', context)

def browse(request):
    return render(request, 'store/browse.html')

def details(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        'game':game,
        'title':"Details"
    }
    return render(request, 'store/details.html', context)

def streams(request):
    return render(request, 'store/streams.html')

def profile(request):
    context = {
        "username":request.user.username,
        "title":"Profile"
    }
    return render(request, 'store/profile.html', context)

def user_login(request):
    context = {
        'title':"User Login",
        "login_form":LoginForm()
    }
    return render(request, 'store/login.html', context)

def signin(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("index")
    else:
        messages.error(request, "Invalid username/password")
        return redirect("login")

def user_register(reqeust):
    context = {
        'title':"User Register",
        "register_form":RegisterForm()
    }
    return render(reqeust, 'store/register.html', context)

def signup(request):
    form = RegisterForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        messages.success(request, "Succesfully created")
        return redirect("login")
    else:
        for error in form.errors:
            messages.error(request, form.errors[error].as_text())
        return redirect("register")

def user_logout(request):
    logout(request)
    return redirect("index")
