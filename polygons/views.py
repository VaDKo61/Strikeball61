from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, FormView

from .forms import PolygonForms
from .models import Polygons


class PolygonsListView(ListView):
    model = Polygons
    template_name = 'polygons/polygons.html'


class PolygonDetailView(DetailView):
    model = Polygons
    template_name = 'polygons/info_polygon.html'


class PolygonFormView(FormView):
    form_class = PolygonForms
    template_name = 'polygons/create_polygon.html'
    success_url = '/polygons'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PolygonEditView(View):

    def get(self, request, slug_polygon):
        polygon = Polygons.objects.get(slug=slug_polygon)
        form = PolygonForms(instance=polygon)
        return render(request, 'polygons/create_polygon.html', context={'form': form})

    def post(self, request, slug_polygon):
        polygon = Polygons.objects.get(slug=slug_polygon)
        form = PolygonForms(request.POST, instance=polygon)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('polygons'))
        return render(request, 'polygons/create_polygon.html', context={'form': form})
