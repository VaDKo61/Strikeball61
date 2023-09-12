from django.contrib import admin
from sunday_games.models import Game


class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('date',)}


admin.site.register(Game, MemberAdmin)
