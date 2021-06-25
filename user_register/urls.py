from django.urls import path
from . import views

# user_register/

app_name = "user_register"
urlpatterns = [
    path("", views.register, name="register")
    # path("<str:team_name>", views.team_details, name="team_details")

]
