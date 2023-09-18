from django import forms

from sunday_games.models import Game


class SundayForms(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
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
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
            'start': forms.TimeInput(attrs={'type': 'start', 'class': 'form-control'}),
        }
