from django.urls import path
from title_list import views

urlpatterns = [
    path('', views.description, name='title'),
]