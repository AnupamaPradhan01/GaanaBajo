from django.urls import path
from .import views

app_name = 'music_app'

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('<int:id>/', views.song_detail, name='song_detail'),
]
