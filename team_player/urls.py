from django.urls import path
from team_player.views import *

urlpatterns = [
    path('', TeamListView.as_view()),
    path('<slug:slug>', DetailTeam.as_view(), name='info_team'),
]
