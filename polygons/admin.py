from django.contrib import admin
from django_admin_geomap import ModelAdmin

from polygons.models import Polygons


class Admin(ModelAdmin):
    geomap_default_latitude = "47.246355"
    geomap_default_longitude = "39.715209"
    geomap_default_zoom = "10"


admin.site.register(Polygons, Admin)
