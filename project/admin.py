from django.contrib import admin
from .models import Team, TeamMember, Board, Column, Tile


class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("team_name", "user_username", "role")


class BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "team_name")


class ColumnAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "team_name", "board_name")


class TileAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "creation_date", "content_type", "content", "multimedia_obj", "column_title",
                    "team_name", "board_name")


# Register your models here.
admin.site.register(Team, TeamAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Tile, TileAdmin)
