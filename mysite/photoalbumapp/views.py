from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import AlbumSerializer, PhotoSerializer, UserSerializer
from .models import Album, Photo

# Create your views here.
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('name')
    serializer_class = AlbumSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by('date_uploaded')
    serializer_class = PhotoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer