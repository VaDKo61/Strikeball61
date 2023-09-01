from django.urls import path
from team_and_players.views import *

urlpatterns = [
    path('', TeamView.as_view()),
]
