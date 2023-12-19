from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Team(models.Model):
    """Team"""
    name = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=200, default='')
    logo = models.ImageField(default='', upload_to='team', blank=True)
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('info_team', args=[self.slug])

    def get_url_edit(self):
        return reverse('team_edit', args=[self.slug])
