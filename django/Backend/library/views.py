from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

from rest_framework import viewsets

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
