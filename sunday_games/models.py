from django.db import models
from django.shortcuts import redirect
from django.urls import reverse

from polygons.models import Polygons


class Game(models.Model):
    date = models.DateField(verbose_name='date')
    polygon = models.ForeignKey(Polygons, on_delete=models.CASCADE, null=True, related_name='games_polygon')
    organizer = models.CharField(max_length=50, default='STRIKE61')
    start = models.TimeField(default='10:00')
    scenario = models.TextField(max_length=10000)
    foto_scenario = models.ImageField(upload_to='sunday_games_scenario', blank=True)
    contribution = models.IntegerField(default=200)
    is_future = models.BooleanField(default=True)
    slug = models.SlugField(default='', null=False)
    result = models.CharField(default='', max_length=1000)

    def __str__(self):
        return f'{self.date} {self.polygon}'

    def get_url(self):
        return reverse('detail_game', args=[self.slug])
