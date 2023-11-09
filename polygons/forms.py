from django import forms
from django.core.exceptions import ValidationError
from pytils.translit import slugify

from polygons.models import Polygons


class PolygonForms(forms.ModelForm):
    """Form of polygon"""
    class Meta:
        model = Polygons
        exclude = ('slug',)
        labels = {
            'name': 'Имя полигона',
            'address': 'Адресс полигона',
            'descriptions': 'Описание полигона',
            'image': 'Фото полигона',
            'image_full': 'Фото полигона',
            'url_yandex': 'Ссылка яндекс',
            'lon': 'Долгота',
            'lat': 'Широта',
        }
        widgets = {
            'address': forms.Textarea(attrs={"cols": "40", "rows": "1"}),
            'descriptions': forms.Textarea(attrs={"cols": "40", "rows": "1"}),
        }

    def clean_name(self):
        """Validate of name(dubla)"""
        data = self.cleaned_data['name']
        objects = Polygons.objects.filter(slug=slugify(data)).exclude(
            id=self.initial['id']) if self.initial else Polygons.objects.filter(slug=slugify(data))
        if objects.exists():
            raise ValidationError(f'Полигон с названием "{data}" уже добавлен')
        return data
