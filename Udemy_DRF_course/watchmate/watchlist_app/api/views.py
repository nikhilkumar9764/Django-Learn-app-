from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from .permissions import *
from .serializers import *
from ..models import *
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.mixins import *
from rest_framework.status import *

# ViewSet has functions like list , retrieve ,


class StreamPlatformVS(viewsets.ViewSet):

    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(obj, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        id = self.kwargs['pk']
        movie = Movie.objects.get(pk=id)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=movie, review_user=review_user)

        if review_queryset.exists():
            raise Exception("Review already given for this movie")

        if movie.num_ratings == 0:
            movie.avg_rating = serializer.validated_data['rating']
        else:
            no_curr = movie.review.count()
            su = MovieSerializer(movie).data
            v1 = su['sum_ratings']
            movie.avg_rating = (v1+serializer.validated_data['rating']) / no_curr+1

        movie.num_ratings = movie.review.count() + 1
        movie.save()
        serializer.save(watchlist=movie, review_user=review_user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]
    throttle_classes = [UserRateThrottle]


class ReviewList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        val1 = self.kwargs['pk']
        return Review.objects.filter(watchlist=val1)
    serializer_class = ReviewSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs, watchlist=self.kwargs['pk'])


class StreamPlatformList(APIView):

    def get(self,request):
        streams = StreamPlatform.objects.all()
        list_movies = StreamPlatformSerializer(streams, many=True, context={'request': request})
        return Response(list_movies.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetail(APIView):
    def get(self, request, pk):
        try:
           streams = StreamPlatform.objects.get(pk=pk)

        except StreamPlatform.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        res_movie = StreamPlatformSerializer(streams, context={'request': request})
        return Response(res_movie.data)

    def put(self,request,pk):
        movie = StreamPlatform.objects.get(pk=pk)
        res_movie_ser = StreamPlatformSerializer(movie, data=request.data)
        if res_movie_ser.is_valid():
            res_movie_ser.save()
            return Response(res_movie_ser.data)
        else:
             return Response(res_movie_ser.errors)

    def delete(self, pk):
        movie = StreamPlatform.objects.get(pk=pk)
        movie.delete()
        return Response(status=HTTP_202_ACCEPTED)


class MovieList(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        movies = Movie.objects.all()
        list_movies = MovieSerializer(movies, many=True)
        return Response(list_movies.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MovieDetail(APIView):

    def get(self, request,pk):
        try :
           movies = Movie.objects.get(pk=pk)

        except Movie.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        res_movie = MovieSerializer(movies)
        return Response(res_movie.data)

    def put(self,request,pk):
        movie = Movie.objects.get(pk=pk)
        res_movie_ser = MovieSerializer(movie, data=request.data)
        if res_movie_ser.is_valid():
            res_movie_ser.save()
            return Response(res_movie_ser.data)
        else:
             return Response(res_movie_ser.errors)

    def delete(self, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=HTTP_202_ACCEPTED)