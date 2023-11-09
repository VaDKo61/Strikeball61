import json
import requests
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from requests import HTTPError

from sunday_games.forms import SundayForms, SundayArchiveForms
from sunday_games.models import *


class GameListView(ListView):
    """Info of all future sunday games"""
    model = Game
    template_name = 'sunday_games/list_games.html'

    def get_queryset(self):
        return Game.objects.filter(is_future=True).order_by('date')


class GameDetailView(DetailView):
    """Info of future sunday game"""
    model = Game
    template_name = 'sunday_games/detail_game.html'

    def get_context_data(self, **kwargs):
        """add the weather for the future game"""
        context = super(GameDetailView, self).get_context_data(**kwargs)
        context['error'] = False
        if self.object.is_future:
            api_key = '7a3670af0bfab65efc9bb9347cc07364'
            lang = 'ru'
            units = 'metric'
            try:
                api_response = requests.get(
                    f'https://api.openweathermap.org/data/2.5/forecast?lat={self.object.polygon.lat}&'
                    f'lon={self.object.polygon.lon}&appid={api_key}&units={units}&lang={lang}')
                api_response.raise_for_status()
            except HTTPError:
                context['error'] = True
            else:
                json_response = json.loads(api_response.text)
                weather_dict = {}
                date_game = str(self.object.date)
                for dict_weather in json_response['list']:
                    if dict_weather['dt_txt'][:10] == date_game:
                        weather_dict[f'time_{dict_weather["dt_txt"][11:13]}'] = {
                            'description': dict_weather['weather'][0]['description'],
                            'temp': round(dict_weather['main']['temp']),
                            'feels_like': round(dict_weather['main']['feels_like']),
                            'visibility': dict_weather['visibility'] // 1000,
                            'speed': round(dict_weather['wind']['speed'], 1),
                            'gust': round(dict_weather['wind']['gust'], 1),
                            'pop': round(dict_weather['pop'] * 100),
                            'rain': dict_weather.get('rain', False),
                            'snow': dict_weather.get('snow', False),
                            'time': dict_weather["dt_txt"][11:16]
                        }
                context['weather_dict'] = weather_dict
        return context


class GameArchiveListView(ListView):
    """Archive of sunday games by year"""
    model = Game
    template_name = 'sunday_games/list_games.html'

    def get_queryset(self):
        """Queryset by year and future"""
        year = self.request.GET.get('year')
        return Game.objects.filter(Q(date__year=year) & Q(is_future=False)).order_by('date')

    def get_context_data(self, **kwargs):
        """Add year in template"""
        context = super(GameArchiveListView, self).get_context_data(**kwargs)
        context['archive'] = True
        context['year'] = self.request.GET.get('year')
        return context


class GameFormView(FormView):
    """Add new sunday game"""
    form_class = SundayForms
    template_name = 'sunday_games/create_game.html'
    success_url = '/sunday_games'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class GameEditView(View):
    """Edit sunday game"""
    def get(self, request, slug_game):
        game = Game.objects.get(slug=slug_game)
        if game.is_future:
            form = SundayForms(instance=game)
        else:
            form = SundayArchiveForms(instance=game)
        return render(request, 'sunday_games/create_game.html', context={'form': form})

    def post(self, request, slug_game):
        game = Game.objects.get(slug=slug_game)
        if game.is_future:
            form = SundayForms(request.POST, request.FILES, instance=game)
        else:
            form = SundayArchiveForms(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detail_game', args=(game.slug,)))
        return render(request, 'sunday_games/create_game.html', context={'form': form})
