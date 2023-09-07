from django.shortcuts import render
from django.views.generic import ListView
from sunday_games.models import *


class GameListView(ListView):
    model = Game
    template_name = 'sunday_games/all_games.html'
