from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', MovieList.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetail.as_view(), name='get_movie_detail'),

    path('', include(router.urls)),

    # path('streams/', StreamPlatformList.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetail.as_view(), name='get_stream_detail'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail')
]