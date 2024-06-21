from django.urls import path
from .import views

app_name = 'music_app'

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('tag/<slug:tag_slug>/', views.song_list, name='song_list_by_tag'),
    path('<int:year>/<slug:song>/', views.song_detail, name='song_detail'),
    path('<int:song_id>/', views.song_share, name='song_share'),
]
