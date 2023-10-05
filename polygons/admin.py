from django.contrib import admin
from django_admin_geomap import ModelAdmin

from polygons.models import Polygons


class Admin(ModelAdmin):
    geomap_default_latitude = '47.2'
    geomap_default_longitude = '39.7'
    geomap_default_zoom = '10.5'


admin.site.register(Polygons, Admin)