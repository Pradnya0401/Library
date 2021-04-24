from django.shortcuts import render
from rest_framework import generics
from library.models import Book
from library.serializers import BookSerializer
# Create your views here.
class BookList(generics.ListCreateAPIView):  #GET & POST
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateAPIView): #update & DELETE
    queryset = Book
    serializer_class = BookSerializer