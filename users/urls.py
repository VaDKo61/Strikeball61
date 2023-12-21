from django.urls import path

from users.views import *

urlpatterns = [
    path('auth/', UserAuthentication.as_view(), name='auth'),
    path('register/', UserRegistration.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile_info, name='profile'),
    path('profile/<str:slug>', ProfileUserView.as_view(), name='profile_user'),
    path('profile/edit/<str:slug>', EditProfileUserView.as_view(), name='edit_profile_user'),
]
