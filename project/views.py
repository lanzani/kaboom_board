from django.http import HttpResponse
from django.shortcuts import render
from .models import Team


# Create your views here.

def index(request):
    return HttpResponse("Hello World")
