from django.shortcuts import render
from django.views.generic import ListView
from team_and_players.models import *


class TeamView(ListView):
    template_name = 'team_and_players/all_team.html'
    model = Team
