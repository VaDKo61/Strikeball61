from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django_admin_geomap import geomap_context

from .forms import PolygonForms
from .models import Polygons


class PolygonsListView(ListView):
    """Info of all polygons"""
    model = Polygons
    template_name = 'polygons/polygons.html'

    def get_context_data(self, **kwargs):
        """Add the parameters to display objects on the map"""
        context = super(PolygonsListView, self).get_context_data(**kwargs)
        for i, j in geomap_context(Polygons.objects.all(), map_longitude='39.7', map_latitude='47.2',
                                   map_zoom='10.5').items():
            context[i] = j
        return context


class PolygonDetailView(DetailView):
    """Info of polygon"""
    model = Polygons
    template_name = 'polygons/info_polygon.html'

    def get_context_data(self, **kwargs):
        """Add the parameters to display on the map"""
        context = super(PolygonDetailView, self).get_context_data(**kwargs)
        for i, j in geomap_context(*kwargs.items(), map_longitude=f"{kwargs['object'].lon}",
                                   map_latitude=f"{kwargs['object'].lat}",
                                   map_zoom='14').items():
            context[i] = j
        return context


class PolygonFormView(PermissionRequiredMixin, FormView):
    """Add new polygon"""
    permission_required = 'polygons.add_polygons'
    form_class = PolygonForms
    template_name = 'polygons/create_polygon.html'
    success_url = '/polygons'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PolygonEditView(View):
    """Edit polygon"""

    def get(self, request, slug_polygon):
        if not request.user.has_perm('polygons.change_polygons'):
            raise PermissionDenied('Нет прав для просмотра данной страницы')
        polygon = Polygons.objects.get(slug=slug_polygon)
        form = PolygonForms(instance=polygon)
        return render(request, 'polygons/create_polygon.html', context={'form': form})

    def post(self, request, slug_polygon):
        polygon = Polygons.objects.get(slug=slug_polygon)
        form = PolygonForms(request.POST, request.FILES, instance=polygon)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('polygon-detail', args=(polygon.slug,)))
        return render(request, 'polygons/create_polygon.html', context={'form': form})


def error_403(request, exception):
    return render(request, '403.html')
