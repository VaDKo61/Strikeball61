from django.db import models
from django.urls import reverse


class Polygons(models.Model):
    name = models.CharField(verbose_name='URL', max_length=50)
    address = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=50, default='Null')
    descriptions = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='polygons/')
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'{self.name}'

    def get_url(self):
        return reverse('polygon-detail', args=[self.slug])

