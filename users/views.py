from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from users.forms import UserRegistrationForm


def auth(request):
    return render(request, 'users/auth.html')


class UserRegistration(FormView):
    """Add new user"""
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
