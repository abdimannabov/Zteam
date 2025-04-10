from django.shortcuts import render
from .models import Games

# Create your views here.
def index(request):
    games = Games.objects.all()
    context = {
        'games':games,
        'title':"Zteam"
    }
    return render(request, 'store/index.html', context)

def browse(request):
    return render(request, 'store/browse.html')

def details(request):
    return render(request, 'store/details.html')

def streams(request):
    return render(request, 'store/streams.html')

def profile(request):
    return render(request, 'store/profile.html')