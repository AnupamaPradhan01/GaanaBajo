from django.shortcuts import render
from .models import Song
#  display song list .


def song_list(request):
    songs = Song.hindi.all()
    return render(request, "song/song_list.html", {'songs': songs})

# display single song


def song_detail(request, id):
    song = Song.hindi.get(id=id)
    return render(request, 'music_app/song/song_detail.html', {'song': song})
