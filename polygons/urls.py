from django.urls import path
from polygons.views import *

urlpatterns = [
    path('', PolygonsListView.as_view(), name='polygons'),
    path('create', PolygonFormView.as_view(), name='polygon-create'),
    path('edit/<str:slug_polygon>', PolygonEditView.as_view(), name='polygon-edit'),
    path('<slug:slug>', PolygonDetailView.as_view(), name='polygon-detail'),
]
