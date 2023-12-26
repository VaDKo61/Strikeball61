from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, FormView

from team_player.forms import TeamForms
from team_player.models import *


class TeamListView(ListView):
    """Info of all team"""
    template_name = 'team_player/all_team.html'
    model = Team


class TeamDetailView(DetailView):
    """Info of team"""
    template_name = 'team_player/info_team.html'
    model = Team


class TeamFormView(PermissionRequiredMixin, FormView):
    """Create new team"""
    permission_required = 'team_player.add_team'
    form_class = TeamForms
    template_name = 'team_player/create_team.html'
    success_url = '/team'

    def form_valid(self, form):
        form.save()
        return super(TeamFormView, self).form_valid(form)


class TeamEditView(View):
    """Edit team"""

    def get(self, request, team_slug):
        if not request.user.has_perm('team_player.change_team'):
            raise PermissionDenied('Нет прав для просмотра данной страницы')
        team = Team.objects.get(slug=team_slug)
        form = TeamForms(instance=team)
        return render(request, 'team_player/create_team.html', context={'form': form})

    def post(self, request, team_slug):
        team = Team.objects.get(slug=team_slug)
        form = TeamForms(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('info_team', args=(team.slug,)))
        return render(request, 'team_player/create_team.html', context={'form': form})


def error_403(request, exception):
    return render(request, '403.html')
