from django.db import models
from django.urls import reverse
from django_admin_geomap import GeoItem
from pytils.translit import slugify


class Polygons(models.Model, GeoItem):
    name = models.CharField(verbose_name='URL', max_length=50)
    address = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='polygons/', blank=True)
    url_yandex = models.CharField(default='', max_length=500)
    slug = models.SlugField(default='', null=False)
    lon = models.FloatField(default='39.715209')
    lat = models.FloatField(default='47.246355')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Polygons, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('polygon-detail', args=[self.slug])

    def get_url_edit(self):
        return reverse('polygon-edit', args=[self.slug])

    @property
    def geomap_longitude(self):
        return '' if self.lon is None else str(self.lon)

    @property
    def geomap_latitude(self):
        return '' if self.lat is None else str(self.lat)
