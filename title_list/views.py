from django.shortcuts import render

from sunday_games.models import Game
from team_player.models import Team
from polygons.models import Polygons


def main_page(request):
    data = {'teams': Team.objects.order_by('?')[:6],
            'polygons': Polygons.objects.order_by('?')[:6],
            'games': Game.objects.filter(is_future=True).order_by('date')[:2],
            }
    return render(request, 'title_list/index.html', context=data)
