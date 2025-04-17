from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm
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
    return render(request, 'store/profile.html')

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