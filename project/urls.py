from django.urls import path
from . import views

# projects/

urlpatterns = [
    path("", views.index, name="index")
]
