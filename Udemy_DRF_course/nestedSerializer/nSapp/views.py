from django.shortcuts import render
from rest_framework import generics
from .serializers import AuthorSerializer, BookSerializer
from django.shortcuts import get_object_or_404
from .models import Author, Book
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
# Create your views here.

class EmployeePagination(PageNumberPagination):
     page_size = 3

class ListEmployees(generics.ListCreateAPIView):
     queryset = Author.objects.all()
     serializer_class = AuthorSerializer
     pagination_class = LimitOffsetPagination
     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['firstName']


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ListBooks(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', '-ratings']
    ordering = ['-ratings']

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer