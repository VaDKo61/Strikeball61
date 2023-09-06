from django.shortcuts import render
from django.views.generic import ListView, DetailView
from team_player.models import *


class TeamListView(ListView):
    template_name = 'team_player/all_team.html'
    model = Team


class DetailTeam(DetailView):
    template_name = 'team_player/info_team.html'
    model = Team

    def get_context_data(self, **kwargs):
        context = super(DetailTeam, self).get_context_data(**kwargs)
        # context['players'] = Player.objects.filter(team_id=self.object)
        context['players'] = Player.objects.all()
        return context
