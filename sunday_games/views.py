from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, FormView

from sunday_games.forms import SundayForms
from sunday_games.models import *


class GameListView(ListView):
    model = Game
    template_name = 'sunday_games/list_games.html'

    def get_queryset(self):
        return Game.objects.filter(is_future=True).order_by('date')


class GameDetailView(DetailView):
    model = Game
    template_name = 'sunday_games/detail_game.html'


class GameArchiveListView(ListView):
    model = Game
    template_name = 'sunday_games/list_games.html'

    def get_queryset(self):
        year = self.request.GET.get('year')
        return Game.objects.filter(Q(date__year=year) & Q(is_future=False)).order_by('date')

    def get_context_data(self, **kwargs):
        context = super(GameArchiveListView, self).get_context_data(**kwargs)
        context['archive'] = True
        context['year'] = self.request.GET.get('year')
        return context


class GameFormView(FormView):
    form_class = SundayForms
    template_name = 'sunday_games/create_game.html'
    success_url = '/sunday_games'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class GameEditView(View):

    def get(self, request, slug_game):
        game = Game.objects.get(slug=slug_game)
        form = SundayForms(instance=game)
        return render(request, 'sunday_games/create_game.html', context={'form': form})

    def post(self, request, slug_game):
        game = Game.objects.get(slug=slug_game)
        form = SundayForms(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detail_game', args=(slug_game, )))
        return render(request, 'sunday_games/create_game.html', context={'form': form})
