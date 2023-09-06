from django.contrib import admin
from team_player.models import Team, Player


class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Team, MemberAdmin)
admin.site.register(Player)
