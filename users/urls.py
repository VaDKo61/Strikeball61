from django.urls import path

from users.views import *

urlpatterns = [
    path('auth/', auth, name='auth'),
    path('register/', UserRegistration.as_view(), name='register'),
]
