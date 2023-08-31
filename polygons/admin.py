from django.contrib import admin
from django.views import generic

from polygons.models import Polygons


class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Polygons, MemberAdmin)
