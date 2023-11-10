from django.shortcuts import render
from django.views.generic import ListView

from sunday_games.models import Game
from team_player.models import Team
from polygons.models import Polygons


class Search(ListView):
    """Search all"""
    template_name = 'title_list/search.html'
    model = Game

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        search = self.request.GET['search']
        context['search'] = search
        Game.objects.all().select_related('polygon').filter(id=1)
        sunday_games = Game.objects.get(polygon__iexact=search)
        context['sunday_games'] = sunday_games
        return context


def main_page(request):
    """Select team, polygons and games"""
    data = {'teams': Team.objects.order_by('?')[:6],
            'polygons': Polygons.objects.order_by('?')[:6],
            'games': Game.objects.filter(is_future=True).order_by('date')[:2],
            }
    return render(request, 'title_list/index.html', context=data)
