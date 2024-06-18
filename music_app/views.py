from django.shortcuts import render
from .models import Song
#  display song list .


def song_list(request):
    songs = Song.hindi.all()
    return render(request, "music_app/song_list.html", {'songs': songs})
