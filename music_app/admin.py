from django.contrib import admin
from .models import Song

# register song models


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'singer', 'publish', 'lang']
