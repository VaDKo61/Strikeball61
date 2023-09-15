from django.contrib import admin
from sunday_games.models import Game


@admin.register(Game)
class MemberAdmin(admin.ModelAdmin):
    ordering = ['date']
    prepopulated_fields = {'slug': ('date',)}
