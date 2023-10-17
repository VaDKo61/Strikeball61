from django import forms
from django.core.exceptions import ValidationError
from pytils.translit import slugify

from team_player.models import Team


class TeamForms(forms.ModelForm):
    class Meta:
        model = Team
        exclude = ('slug',)
        labels = {
            'name': 'Имя команды',
            'descriptions': 'Описание',
            'logo': 'Логотип команды',
        }
        widgets = {
            'descriptions': forms.Textarea(attrs={"cols": "40", "rows": "5"})
        }

    def clean_name(self):
        data = self.cleaned_data['name']
        objects = Team.objects.filter(slug=slugify(data)).exclude(
            id=self.initial['id']) if self.initial else Team.objects.filter(slug=slugify(data))
        if objects.exists():
            raise ValidationError(f'Команда с именем "{data}" уже зарегестрирована')
        return data
