from django import template
from ..models import Song

register = template.Library()


@register.simple_tag
def total_songs():
    return Song.hindi.count()


@register.inclusion_tag('music_app/song/latest_songs.html')
def show_latest_songs(count=5):
    latest_songs = Song.hindi.order_by('-publish')[:count]
    return {'latest_songs': latest_songs}


@register.inclusion_tag('music_app/song/top_artists.html')
def show_top_artists(count=5):
    top_artists = Song.hindi.order_by('-name')[:count]
    return {'top_artists': top_artists}
