from django.shortcuts import render
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