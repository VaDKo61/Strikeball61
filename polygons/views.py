from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Polygons


class ListPolygons(ListView):
    model = Polygons
    template_name = 'polygons/polygons.html'


class DetailPolygons(DetailView):
    model = Polygons
    template_name = 'polygons/info_polygon.html'

