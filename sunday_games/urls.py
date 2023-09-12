from django.urls import path
from sunday_games.views import *

urlpatterns = [
    path('', GameListView.as_view(), name='sunday_games'),
    path('<str:slug>', GameDetailView.as_view(), name='detail_game'),
]