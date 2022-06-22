from django.shortcuts import render

from .models import Movie
from django.http import JsonResponse
# Create your views here.

def list_all(request):
    movies = Movie.objects.all()
    list_movies = list(movies.values())
    data = {
        'movies': list_movies
    }
    return JsonResponse(data)

def get_item(request, pk):
    movies = Movie.objects.get(pk=pk)
    data = {
        'name': movies.name,
        'description': movies.description,
        'is_active': movies.is_active
    }
    return JsonResponse(data)