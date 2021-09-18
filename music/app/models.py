from django.contrib.auth import get_user_model
from django.db import models

# from django.contrib.auth.models import User

User = get_user_model()


# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Album(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey("Singer", on_delete=models.CASCADE, related_name="singer")

    def __str__(self):
        return f"{self.title}"


class Track(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="album")

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    body = models.CharField(max_length=100)
    track = models.ForeignKey("Track", on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class T1(models.Model):
    t1 = models.CharField(max_length=100)


class Throgh(models.Model):
    mid = models.CharField(max_length=100)
    toT1 = models.ForeignKey(T1, on_delete=models.CASCADE)
    toT2 = models.ForeignKey("T2", on_delete=models.CASCADE)


class T2(models.Model):
    m2m = models.ManyToManyField(to=T1, through=Throgh, limit_choices_to=2)
    t2 = models.CharField(max_length=100)
    _tryHide = models.CharField(max_length=100) ## dar jaye dg rahat neshoonesh nadad
