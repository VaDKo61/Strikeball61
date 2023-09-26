from django import forms

from polygons.models import Polygons


class PolygonForms(forms.ModelForm):
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
