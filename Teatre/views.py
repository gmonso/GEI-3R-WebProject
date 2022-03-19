from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'cinemas/home.html')

def CinemaList(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas':cinemas}
    return render(request, 'Cinema/List.html', json)

def MovieDetail(request):
    movies = Movie.objects.all()
    json = {'movies':movies}
    return render(request, 'Movie/Detail.html', json)

def MovieList(request):
    movies = Movie.objects.all()
    json = {'movies': movies}
    return render(request, 'Movie/List.html', json)

def SignIn(request):
    return render(request, 'cinemas/SignIn.html')