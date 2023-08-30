from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from polygons.views import ListPolygons

urlpatterns = [
    path('', ListPolygons.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
