from django.urls import path
from sunday_games.views import *

urlpatterns = [
    path('', GameListView.as_view())
]