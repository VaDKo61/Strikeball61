from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Polygons


class PolygonsListView(ListView):
    model = Polygons
    template_name = 'polygons/polygons.html'


class PolygonsDetailView(DetailView):
    model = Polygons
    template_name = 'polygons/info_polygon.html'

