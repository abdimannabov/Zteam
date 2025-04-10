from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def browse(request):
    return render(request, 'store/browse.html')

def details(request):
    return render(request, 'store/details.html')

def streams(request):
    return render(request, 'store/streams.html')

def profile(request):
    return render(request, 'store/profile.html')