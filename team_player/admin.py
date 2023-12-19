from django.contrib import admin
from team_player.models import Team


class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Team, MemberAdmin)

