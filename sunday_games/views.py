from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sunday_games.models import *


class GameListView(ListView):
    model = Game
    template_name = 'sunday_games/future_games.html'


class GameDetailView(DetailView):
    model = Game
    template_name = 'sunday_games/detail_game.html'

    # def get_context_data(self, **kwargs):
    #     context = super(GameListView, self).get_context_data(**kwargs)
    #     context['polygonse'] = Polygons.objects.all()
    #     return context
