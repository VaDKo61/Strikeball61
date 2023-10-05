from django import forms

from sunday_games.models import Game


class SundayForms(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('date', 'is_future', 'slug')
        labels = {
            'polygon': 'Полигон',
            'organizer': 'Организатор',
            'start': 'Начало игры',
            'scenario': 'Сценарий',
            'foto_scenario': 'Фото сценария',
            'contribution': 'Взнос',
            'result': 'Результат',
            'result_foto': 'Фотографии с игры',
        }
        widgets = {
            'date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'scenario': forms.Textarea(attrs={"cols": "80", "rows": "30"}),
            'result_foto': forms.Textarea(attrs={"cols": "80", "rows": "3"}),
        }


class SundayArchiveForms(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('result', 'result_foto')
        labels = {
            'result': 'Результат',
            'result_foto': 'Фотографии с игры',
        }
        widgets = {
            'result': forms.Textarea(attrs={"cols": "80", "rows": "30"}),
            'result_foto': forms.Textarea(attrs={"cols": "80", "rows": "3"}),
        }
