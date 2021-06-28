from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Team, TeamMember, Board, Column, Tile
from .forms import CreateTeam


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user_teams = TeamMember.objects.filter(user_username=request.user)
        return render(request, "project/index.html", {"user_teams": user_teams})

    else:

        return HttpResponseRedirect("/login")


def team_details(request, team_name):
    # Qui è la pagina del team, vengono mostrati membri e boards

    # team = get_object_or_404(Team, pk=team_name)
    try:
        team = Team.objects.get(pk=team_name)
    except Team.DoesNotExist:
        return HttpResponseRedirect("/project")

    try:
        boards = Board.objects.filter(team_name=team)
    except Board.DoesNotExist:
        pass

    try:
        members = TeamMember.objects.filter(team_name=team)
    except TeamMember.DoesNotExist:
        pass

    # Se l'utente corrente non è nel team selezionato reindirizza a pagina dei suoi team
    if not TeamMember.objects.filter(team_name=team, user_username=request.user).exists():
        return HttpResponseRedirect("/project")

    user_admin = TeamMember.objects.get(team_name=team, user_username=request.user)

    if request.method == "POST":
        if request.POST.get("new_board"):
            board_name = request.POST.get("board_name")
            board_description = request.POST.get("board_description")

            board_already_exist = (
                    len(Board.objects.filter(name=board_name, team_name=team)) > 0
            )

            if board_already_exist:
                print(f"[INVALID] La board {board_name} esiste già")
            elif 45 >= len(board_name) > 0 and len(board_description) <= 255:
                b = Board(name=board_name, description=board_description, team_name=team)
                b.save()
            else:
                print("[INVALID] Il nome può essere lungo max 45 caratteri e la descrizione max 255 caratteri")

        elif request.POST.get("delete_board"):
            board_name = request.POST.get("delete_board")
            Board.objects.filter(name=board_name, team_name=team).delete()

        elif request.POST.get("delete_team"):
            Team.objects.filter(name=team.name).delete()

        return HttpResponseRedirect("/project/%s" % team.name)

    return render(request, "project/team_details.html",
                  {"team": team, "boards": boards, "members": members, "user_admin": user_admin})


def create_team(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CreateTeam(request.POST)
            if not form.is_valid():
                return render(request, "project/create_team.html", {"form": form})

            team_name = form.cleaned_data["name"]
            team_description = form.cleaned_data["description"]

            team_already_exist = (
                    len(Team.objects.filter(name=team_name)) > 0
            )
            if not team_already_exist:
                # Aggiunta Team
                team = Team(name=team_name, description=team_description)
                team.save()

                # Aggiunta Team Member
                team_admin = request.user
                team_member = TeamMember(team_name=team, user_username=team_admin, role="a")
                team_member.save()

            return HttpResponseRedirect("/project/%s" % team_name)
        else:
            form = CreateTeam()
        return render(request, "project/create_team.html", {"form": form})
    else:
        return HttpResponseRedirect("/login")


def board_details(request, team_name, board_name):
    try:
        team = Team.objects.get(pk=team_name)
    except Team.DoesNotExist:
        return HttpResponseRedirect("/project")
    try:
        board = Board.objects.get(team_name=team, name=board_name)
    except Board.DoesNotExist:
        return HttpResponseRedirect("/project/%s" % team_name)

    try:
        members = TeamMember.objects.filter(team_name=team)
    except TeamMember.DoesNotExist:
        pass

    # Se l'utente corrente non è nel team selezionato reindirizza a pagina dei suoi team
    if not TeamMember.objects.filter(team_name=team, user_username=request.user).exists():
        return HttpResponseRedirect("/project")

    try:
        columns = Column.objects.filter(team_name=team, board_name=board)
    except Column.DoesNotExist:
        pass

    try:
        tiles = Tile.objects.filter(team_name=team, board_name=board)
    except Tile.DoesNotExist:
        pass

    return render(request, "project/board_details.html", {"columns": columns, "tiles": tiles})


def view_profile(request):
    return render(request, "project/view_profile.html", {})
