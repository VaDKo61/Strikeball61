from django import forms
from django.core.exceptions import ValidationError
from pytils.translit import slugify

from sunday_games.models import Game


class SundayForms(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('is_future', 'slug')
        labels = {
            'date': 'Дата',
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

    def clean(self):
        cleaned_data = super(SundayForms, self).clean()
        date = cleaned_data['date']
        polygon = cleaned_data['polygon']
        if date and polygon:
            if slugify(f'{date} {polygon}') in [game.slug for game in Game.objects.all()]:
                raise ValidationError('Игра на данную дату на данном полигоне уже запланирована')


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
