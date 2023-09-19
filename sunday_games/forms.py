from django import forms

from sunday_games.models import Game


class SundayForms(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('is_future', 'slug', 'result')
        labels = {
            'date': 'Дата',
            'polygon': 'Полигон',
            'organizer': 'Организатор',
            'start': 'Начало игры',
            'scenario': 'Сценарий',
            'foto_scenario': 'Фото сценария',
            'contribution': 'Взнос',
            'result': 'Результат',
        }
        widgets = {
            'date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            'start': forms.TimeInput(attrs={'type': 'time'}),
        }
