from django.shortcuts import render, get_object_or_404
from .models import Song
#  display song list .


def song_list(request):
    songs = Song.hindi.all()
    return render(request, "music_app/song/song_list.html", {'songs': songs})

# display single song


def song_detail(request, id):
    song = get_object_or_404(Song, id=id, lang=Song.Languages.HINDI)
    return render(request, 'music_app/song/song_detail.html', {'song': song})
