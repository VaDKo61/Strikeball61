from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sunday_games.models import *


class GameListView(ListView):
    queryset = Game.objects.filter(is_future=True)
    template_name = 'sunday_games/future_games.html'

    def get_context_data(self, **kwargs):
        context = super(GameListView, self).get_context_data(**kwargs)
        context['game'] = Game.objects.all()[0]
        return context


class GameDetailView(DetailView):
    model = Game
    template_name = 'sunday_games/detail_game.html'


class GameArchiveListView(ListView):
    queryset = Game.objects.filter(is_future=False)
    template_name = 'sunday_games/archive_game.html'


    # def get_context_data(self, **kwargs):
    #     context = super(GameListView, self).get_context_data(**kwargs)
    #     context['polygonse'] = Polygons.objects.all()
    #     return context
