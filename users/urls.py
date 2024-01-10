from django.urls import path

from users.views import *

urlpatterns = [
    path('auth/', UserAuthenticationView.as_view(), name='auth'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('profile/password_reset', UserPasswordResetView.as_view(), name='password_reset_user'),
    path('profile/password_reset_done', password_reset_done_user, name='password_reset_done'),
    path('profile/set_new_password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('profile/set_new_password_done', set_new_password_done, name='set_new_password_done'),
    path('profile/<str:slug>', ProfileUserView.as_view(), name='profile_user'),
    path('profile/edit/<str:slug>', EditProfileUserView.as_view(), name='edit_profile_user'),
]

handler403 = 'users.views.error_403'
