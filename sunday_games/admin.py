from django.contrib import admin
from sunday_games.models import Game


@admin.register(Game)
class MemberAdmin(admin.ModelAdmin):
    exclude = ['slug', 'result', 'is_future']
    ordering = ['date']
