from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, ListView, DetailView

from sunday_games.models import Game
from users.forms import UserRegistrationForm, UserAuthenticationForm, UserEditForm, UserInfoEditForm
from users.models import UserInfo


class UserRegistration(FormView):
    """Add new user"""
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        new_user = UserInfo(user=User.objects.get(username=form.cleaned_data['username']), team_id=11)
        new_user.save()
        user = authenticate(self.request, username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'])
        login(self.request, user)
        return super().form_valid(form)


class UserAuthentication(LoginView):
    """Authentication user"""
    template_name = 'users/auth.html'


class ProfileUserView(DetailView):
    """Info obout user"""
    model = UserInfo
    template_name = 'users/profile_user.html'


class EditProfileUserView(View):
    """Edit user"""

    def get(self, request, slug):
        if not request.user.has_perm('users.change_userinfo'):
            raise PermissionDenied('Нет прав для просмотра данной страницы')
        user_info = UserInfo.objects.get(slug=slug)
        form_userinfo = UserInfoEditForm(instance=user_info)
        user = User.objects.get(id=user_info.user_id)
        form_user = UserEditForm(instance=user)
        return render(request, 'users/edit_profile.html',
                      context={'form_userinfo': form_userinfo, 'form_user': form_user})

    def post(self, request, slug):
        user_info = UserInfo.objects.get(slug=slug)
        user = User.objects.get(id=user_info.user_id)
        form_userinfo = UserInfoEditForm(request.POST, request.FILES, instance=user_info)
        form_user = UserEditForm(request.POST, instance=user)
        if form_userinfo.is_valid():
            if form_user.is_valid():
                form_userinfo.save()
                form_user.save()
                return HttpResponseRedirect(reverse('profile_user', args=(user_info.slug,)))
        else:
            return render(request, 'users/edit_profile.html',
                          context={'form_userinfo': form_userinfo, 'form_user': form_user})


def logout_user(request):
    logout(request)
    return redirect('auth')


def error_403(request, exception):
    return render(request, '403.html')
