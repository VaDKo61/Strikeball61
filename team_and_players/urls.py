from django.urls import path
from team_and_players.views import *

urlpatterns = [
    path('', TeamView.as_view()),
    path('<slug:slug>', DetailTeam.as_view(), name='info_team'),
]
