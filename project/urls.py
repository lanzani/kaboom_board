from django.urls import path
from . import views

# projects/

app_name = "project"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:team_name>", views.team_details, name="team_details")
]
