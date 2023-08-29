from django.shortcuts import render
from django.urls import reverse


def choose_poligons(request):
    return render(request, 'polygons/polygons.html')