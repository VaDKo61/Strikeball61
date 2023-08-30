from django.db import models


class Polygons(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=50, default='Null')
    descriptions = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')
