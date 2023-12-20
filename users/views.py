from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, DetailView

from sunday_games.models import Game
from users.forms import UserRegistrationForm, UserAuthenticationForm
from users.models import UserInfo


class UserRegistration(FormView):
    """Add new user"""
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserAuthentication(LoginView):
    """Authentication user"""
    template_name = 'users/auth.html'


def profile_info(request):
    return render(request, 'users/profile.html')


def logout_user(request):
    logout(request)
    return redirect('auth')
