from django.shortcuts import render, get_object_or_404
from .models import Song
from .forms import EmailSongForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count
#  display song list .


def song_list(request, tag_slug=None):
    songs = Song.hindi.all()
    # filter songs by tag
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        songs = songs.filter(tags__in=[tag])
    return render(request, "music_app/song/song_list.html", {'songs': songs, 'tag': tag})

# display single song


def song_detail(request, year, song):
    song = get_object_or_404(
        Song,  lang=Song.Languages.HINDI,  publish__year=year, slug=song,)
    # list of similar songs
    song_tags_ids = song.tags.values_list('id', flat=True)
    similar_songs = Song.hindi.filter(
        tags__in=song_tags_ids)\
        .exclude(id=song.id)
    similar_songs = similar_songs.annotate(same_tags=Count('tags'))\
        .order_by('-same_tags', '-publish')[:4]
    return render(request, 'music_app/song/song_detail.html', {'song': song, 'similar_songs': similar_songs})

# song share via email


def song_share(request, song_id):
    # retrieve post by id
    song = get_object_or_404(Song,  lang=Song.Languages.HINDI, id=song_id)

    sent = False
    if request.method == 'POST':
        # form was submitted
        form = EmailSongForm(request.POST)
        if form.is_valid():
            # form fields passed validation
            cd = form.cleaned_data
            # .....send email
            song_url = request.build_absolute_uri(song.get_absolute_url())
            subject = f"{cd['name']} recommends you to listen "\
                f"{song.name}"
            message = f"Listen{song.name} at {song_url}\n\n"\
                f"{cd['name']}\'s comments:{cd['comments']}"
            send_mail(subject, message,
                      'anupama13pradhan@gmail.com', [cd['to']])

            sent = True
    else:
        form = EmailSongForm()
    return render(request, 'music_app/song/song_share.html', {'song': song, 'sent': sent, 'form': form})
