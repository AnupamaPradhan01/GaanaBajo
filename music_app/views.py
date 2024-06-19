from django.shortcuts import render, get_object_or_404
from .models import Song
from .forms import EmailSongForm
#  display song list .


def song_list(request):
    songs = Song.hindi.all()
    return render(request, "music_app/song/song_list.html", {'songs': songs})

# display single song


def song_detail(request, year, song):
    song = get_object_or_404(
        Song,  lang=Song.Languages.HINDI,  publish__year=year, slug=song,)
    return render(request, 'music_app/song/song_detail.html', {'song': song})

# song share via email


def song_share(request, song_id):
    # retrieve post by id
    song = get_object_or_404(Song, id=song_id, lang=Song.Languages.HINDI)
    if request.method == 'POST':
        # form was submitted
        form = EmailSongForm(request.POST)
        if form.is_valid():
            # form fields passed validation
            cd = form.cleaned_data
            # .....send email
    else:
        form = EmailSongForm()
    return render(request, 'music_app/song/song_share.html')
