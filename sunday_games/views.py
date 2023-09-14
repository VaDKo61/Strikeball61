from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sunday_games.models import *


class GameListView(ListView):
    model = Game
    template_name = 'sunday_games/future_games.html'

    def get_queryset(self):
        query = self.request.GET.get('button')
        return Game.objects.filter(is_future=True)


class GameDetailView(DetailView):
    model = Game
    template_name = 'sunday_games/detail_game.html'


class GameArchiveListView(ListView):
    model = Game
    template_name = 'sunday_games/archive_game.html'

    def get_queryset(self):
        year = self.request.GET.get('year')
        return Game.objects.filter(Q(date__year=year) & Q(is_future=False))

    # def get_context_data(self, **kwargs):
    #     context = super(GameListView, self).get_context_data(**kwargs)
    #     context['polygonse'] = Polygons.objects.all()
    #     return context
