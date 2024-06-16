from django.db import models
from django.utils import timezone

# song model.


class Song(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    album = models.CharField(max_length=250)
    singer = models.CharField(max_length=250)
    year = models.IntegerField()
    song_img = models.ImageField(upload_to='images/')
    song_file = models.FileField(upload_to='uploads/')
    publish = models.DateTimeField(default=timezone.now)
