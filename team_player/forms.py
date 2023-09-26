from django import forms

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