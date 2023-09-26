from django import forms

from polygons.models import Polygons


class PolygonForms(forms.ModelForm):
    class Meta:
        model = Polygons
        exclude = ('slug',)
        labels = {
            'name': 'Имя полигона',
            'address': 'Адресс полигона',
            'coordinates': 'Координаты полигона',
            'descriptions': 'Описание полигона',
            'image': 'Фото полигона',
            'image_full': 'Фото полигона',
            'url_yandex': 'Ссылка яндекс',
        }
        widgets = {
            'address': forms.Textarea(attrs={"cols": "40", "rows": "1"}),
            'descriptions': forms.Textarea(attrs={"cols": "40", "rows": "1"}),
        }
