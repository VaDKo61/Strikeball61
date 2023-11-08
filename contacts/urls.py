from django.urls import path

from contacts.views import get_contacts

urlpatterns = [
    path('', get_contacts, name='contacts')
]