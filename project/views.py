from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Team, TeamMember
from .forms import CreateTeam


# Create your views here.

def index(request):
    teams = Team.objects.all()

    return render(request, "project/index.html", {"teams": teams})


def team_details(request, team_name):
    # Qui è la pagina del team, vengono mostrati membri e boards
    # try:
    #     team = Team.objects.get(pk=team_name)
    #
    #     return render(request, "project/team_details.html", {"team": team})
    # except Team.DoesNotExist:
    #     raise Http404()
    team = get_object_or_404(Team, pk=team_name)
    return render(request, "project/team_details.html", {"team": team})


def create_team(request):
    # TODO se l'utente non è autenticato non può creare il team
    if request.method == "POST":
        form = CreateTeam(request.POST)
        if not form.is_valid():
            return render(request, "project/create_team.html", {"form": form})

        # Aggiunta Team
        team_name = form.cleaned_data["name"]
        team_description = form.cleaned_data["description"]
        team = Team(name=team_name, description=team_description)
        team.save()

        # Aggiunta Team Member
        team_admin = request.user
        team_member = TeamMember(team_name=team, user_username=team_admin, role="a")
        team_member.save()

        return HttpResponseRedirect("/project/%s" % team.name)
    else:
        form = CreateTeam()
    return render(request, "project/create_team.html", {"form": form})
