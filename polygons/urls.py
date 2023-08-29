from django.urls import path
from polygons.views import choose_poligons

urlpatterns = [
    path('', choose_poligons),
]