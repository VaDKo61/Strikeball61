from datetime import datetime

from django.db import models
from django.urls import reverse

from pytils.translit import slugify
from polygons.models import Polygons


class Game(models.Model):
    organizer_choose = [('STRIKE61', 'STRIKE61'),
                        ]
    date = models.DateField(verbose_name='date')
    polygon = models.ForeignKey(Polygons, on_delete=models.CASCADE, null=True, related_name='games_polygon')
    organizer = models.CharField(max_length=50, choices=organizer_choose, default='STRIKE61')
    start = models.TimeField(default='10:00')
    scenario = models.TextField(default='Будет позже', max_length=10000)
    foto_scenario = models.ImageField(upload_to='sunday_games_scenario', blank=True)
    contribution = models.IntegerField(default=200)
    is_future = models.BooleanField(default=True)
    slug = models.SlugField(default='', null=False)
    result = models.CharField(default='', max_length=5000, blank=True)
    result_foto = models.CharField(default='Фотографии будут позже', max_length=500, blank=True)

    def __str__(self):
        return f'{self.date} {self.polygon}'

    def save(self, *args, **kwargs):
        self.is_future = True if self.date >= datetime.now().date() else False
        self.slug = slugify(f'{self.date} {self.polygon}')
        super(Game, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('detail_game', args=[self.slug])

    def get_url_edit(self):
        return reverse('edit_game', args=[self.slug])
