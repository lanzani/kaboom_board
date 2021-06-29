from django.urls import path
from . import views

# project/

app_name = "project"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:team_name>", views.team_details, name="team_details"),
    path("<str:team_name>/<str:board_name>", views.board_details, name="board_details"),
    path("<str:team_name>/<str:board_name>/archive", views.view_board_archive, name="view_board_archive"),

    path("view_profile/", views.view_profile, name="view_profile")
]
