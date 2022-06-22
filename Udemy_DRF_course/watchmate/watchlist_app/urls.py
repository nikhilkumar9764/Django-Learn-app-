from django.urls import path, include
from .views import *

urlpatterns = [
    path('list/', list_all, name='movie-list'),
    path('<int:pk>/', get_item, name='get_movie_detail')
]