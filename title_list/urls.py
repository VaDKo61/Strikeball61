from django.urls import path
from title_list.views import *

urlpatterns = [
    path('', main_page, name='title'),
]