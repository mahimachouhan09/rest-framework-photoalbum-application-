from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Album,Photo

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id','username','email')

class PhotoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Photo
    fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
  # photos = serializers.StringRelatedField(many=True)
  photos = PhotoSerializer(many=True, read_only=True)
  class Meta:
    model = Album
    fields = '__all__'