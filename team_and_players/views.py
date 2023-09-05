from django.shortcuts import render
from django.views.generic import ListView, DetailView
from team_and_players.models import *


class TeamView(ListView):
    template_name = 'team_and_players/all_team.html'
    model = Team


class DetailTeam(DetailView):
    template_name = 'team_and_players/info_team.html'
    model = Team
