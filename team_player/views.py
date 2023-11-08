from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, FormView

from team_player.forms import TeamForms
from team_player.models import *


class TeamListView(ListView):
    template_name = 'team_player/all_team.html'
    model = Team


class TeamDetailView(DetailView):
    template_name = 'team_player/info_team.html'
    model = Team

    def get_context_data(self, **kwargs):
        """Add the players"""
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        context['players'] = Player.objects.all()
        return context


class TeamFormView(FormView):
    form_class = TeamForms
    template_name = 'team_player/create_team.html'
    success_url = '/team'

    def form_valid(self, form):
        form.save()
        return super(TeamFormView, self).form_valid(form)


class TeamEditView(View):

    def get(self, request, team_slug):
        team = Team.objects.get(slug=team_slug)
        form = TeamForms(instance=team)
        return render(request, 'team_player/create_team.html', context={'form': form})

    def post(self, request, team_slug):
        team = Team.objects.get(slug=team_slug)
        form = TeamForms(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('info_team', args=(team.slug, )))
        return render(request, 'team_player/create_team.html', context={'form': form})
