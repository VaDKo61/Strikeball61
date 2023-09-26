from django.urls import path
from team_player.views import *

urlpatterns = [
    path('', TeamListView.as_view(), name='team'),
    path('create', TeamFormView.as_view(), name='team_create'),
    path('edit/<str:team_slug>', TeamEditView.as_view(), name='team_edit'),
    path('<slug:slug>', TeamDetailView.as_view(), name='info_team'),
]
