from django.shortcuts import render, get_object_or_404
from .models import Song
#  display song list .


def song_list(request):
    songs = Song.hindi.all()
    return render(request, "music_app/song/song_list.html", {'songs': songs})

# display single song


def song_detail(request, year, song):
    song = get_object_or_404(
        Song,  lang=Song.Languages.HINDI,  publish__year=year, slug=song,)
    return render(request, 'music_app/song/song_detail.html', {'song': song})
