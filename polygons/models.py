from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Polygons(models.Model):
    name = models.CharField(verbose_name='URL', max_length=50)
    address = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=50, default='')
    descriptions = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='polygons/', blank=True)
    image_full = models.ImageField(upload_to='polygons/full', default='', blank=True)
    url_yandex = models.CharField(default='', max_length=500)
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Polygons, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('polygon-detail', args=[self.slug])

    def get_url_edit(self):
        return reverse('polygon-edit', args=[self.slug])
