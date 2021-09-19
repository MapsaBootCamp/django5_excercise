from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Singer (models.Model):
    name = models.CharField(max_length=255)

class Album(models.Model):
    title = models.CharField(max_length=255)
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='singer')


class Track(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE,related_name='album')
    title = models.CharField(max_length=255)


class Comment(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE , related_name='track')
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='user')
    content = models.TextField(null=True,blank=True)