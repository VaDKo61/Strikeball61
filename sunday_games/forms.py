from django import forms

from sunday_games.models import Game


class SundayForms(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('date', 'is_future', 'slug', 'result')
        labels = {
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
            'scenario': forms.Textarea(attrs={"cols": "80", "rows": "30"})
        }
