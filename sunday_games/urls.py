from django.urls import path
from sunday_games.views import *

urlpatterns = [
    path('', GameListView.as_view(), name='sunday_games'),
    path('detail/<str:slug>', GameDetailView.as_view(), name='detail_game'),
    path('archive', GameArchiveListView.as_view(), name='archive_game'),
    path('create', GameFormView.as_view(), name='create_game'),
    path('edit/<str:slug_game>', GameEditView.as_view(), name='edit_game'),
]