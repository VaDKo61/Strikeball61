from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView, ListView, DetailView

from sunday_games.models import Game
from users.forms import UserRegistrationForm, UserAuthenticationForm, UserEditForm, UserInfoEditForm, UserPasswordReset
from users.models import UserInfo


class UserRegistrationView(FormView):
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


class UserAuthenticationView(LoginView):
    """Authentication user"""
    template_name = 'users/auth.html'


class ProfileUserView(DetailView):
    """Info obout user"""
    model = UserInfo
    template_name = 'users/profile_user.html'


class EditProfileUserView(View):
    """Edit user"""

    def get(self, request, slug):
        if request.user.username != slug:
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


class UserPasswordResetView(PasswordResetView):
    """Reset password"""
    template_name = 'users/reset_password.html'
    success_url = reverse_lazy('password_reset_done')


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/set_new_password.html'
    success_url = reverse_lazy('set_new_password_done')


def logout_user(request):
    logout(request)
    return redirect('auth')


def error_403(request, exception):
    return render(request, '403.html')


def password_reset_done_user(request):
    return render(request, 'users/reset_password_done.html')


def set_new_password_done(request):
    return render(request, 'users/set_new_password_done.html')
