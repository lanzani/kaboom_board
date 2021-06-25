from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Team


# Create your views here.

def index(request):
    teams = Team.objects.all()
    return render(request, "project/index.html", {"teams": teams})


def team_details(request, team_name):
    # try:
    #     team = Team.objects.get(pk=team_name)
    #
    #     return render(request, "project/team_details.html", {"team": team})
    # except Team.DoesNotExist:
    #     raise Http404()
    team = get_object_or_404(Team, pk=team_name)
    return render(request, "project/team_details.html", {"team": team})
