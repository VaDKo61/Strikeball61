from django.db import models
from polygons.models import Polygons


class Game(models.Model):
    date = models.DateField()
    polygon = models.OneToOneField(Polygons, on_delete=models.CASCADE, primary_key=True, related_name='games_polygon')
    organizer = models.CharField(max_length=50, default='STRIKE61')
    start = models.TimeField(default=None)
    scenario = models.CharField(max_length=500)
    contribution = models.IntegerField(default=200)
    foto_games = models.ImageField(upload_to='sunday_games', blank=True)
    is_future = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.date} {self.polygon}'
