from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s "% self.name

class Photo(models.Model):
    album = models.ForeignKey(Album , related_name = 'photos', on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    photo = models.URLField(max_length=200)
    title = models.CharField(max_length=25,default ='')
    description = models.CharField(max_length=25 ,default ='')
    date_uploaded = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     return "%s "% self.title