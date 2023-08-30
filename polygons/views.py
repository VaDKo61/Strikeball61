from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from .models import Polygons


class ListPolygons(ListView):
    model = Polygons
    template_name = 'polygons/polygons.html'
