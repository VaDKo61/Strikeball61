from django.db import models
from django.shortcuts import redirect
from django.urls import reverse

from polygons.models import Polygons


class Game(models.Model):
    date = models.DateField(verbose_name='date')
    polygon = models.ForeignKey(Polygons, on_delete=models.CASCADE, null=True, related_name='games_polygon')
    organizer = models.CharField(max_length=50, default='STRIKE61')
    start = models.TimeField(default='10:00')
    scenario = models.CharField(max_length=500)
    contribution = models.IntegerField(default=200)
    foto_games = models.ImageField(upload_to='sunday_games', blank=True)
    is_future = models.BooleanField(default=True)
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'{self.date} {self.polygon}'

    def get_url(self):
        return reverse('detail_game', args=[self.slug])

    def get_url_archive(self):
        return redirect('archive_game')
