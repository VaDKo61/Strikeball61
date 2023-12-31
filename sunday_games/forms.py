from django import forms
from django.core.exceptions import ValidationError
from pytils.translit import slugify

from sunday_games.models import Game


class SundayForms(forms.ModelForm):
    """Form of sunday game"""
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
        """Validate of date and polygon(dubla)"""
        cleaned_data = super(SundayForms, self).clean()
        date = cleaned_data['date']
        polygon = cleaned_data['polygon']
        if date and polygon:
            objects = Game.objects.exclude(id=self.initial['id']) if self.initial else Game.objects.all()
            if slugify(f'{date} {polygon}') in [game.slug for game in objects]:
                raise ValidationError(f'Игра на {date.strftime("%d.%m.%Y")} на полигоне "{polygon}" уже запланирована')


class SundayArchiveForms(forms.ModelForm):
    """Form of archive sunday game"""
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
