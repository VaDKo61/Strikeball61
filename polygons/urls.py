from django.urls import path
from polygons.views import ListPolygons, DetailPolygons

urlpatterns = [
    path('', ListPolygons.as_view(), name='polygons'),
    path('detail/<slug:slug>', DetailPolygons.as_view(), name='polygon-detail'),
]
