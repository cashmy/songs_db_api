from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.SongList.as_view()),
    path('songs/<int:song_id', views.SongDetail.as_view()),
]
