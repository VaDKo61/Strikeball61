from django.urls import path
from polygons.views import *

urlpatterns = [
    path('', PolygonsListView.as_view(), name='polygons'),
    path('<slug:slug>', PolygonsDetailView.as_view(), name='polygon-detail'),
]
