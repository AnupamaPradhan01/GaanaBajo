from django.db import models
from django.utils import timezone

# song model.


class Song(models.Model):
    # adding a status field for language choice
    class Languages(models.TextChoices):
        HINDI = 'H', 'Hindi'
        ENGLISH = 'E', 'English'

    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    album = models.CharField(max_length=250)
    singer = models.CharField(max_length=250)
    year = models.IntegerField()
    song_img = models.ImageField(upload_to='images/')
    song_file = models.FileField(upload_to='uploads/')
    publish = models.DateTimeField(default=timezone.now)
    lang = models.CharField(
        max_length=2, choices=Languages.choices, default=Languages.HINDI)

    # defining default sort order(reverse chronological order)from newest to oldest
    class Meta:
        ordering = ['-publish']
        # adding a database index for queries filtering or ordering
        indexes = [models.Index(fields=['-publish']),]
