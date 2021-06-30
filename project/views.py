from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Team, TeamMember, Board, Column, Tile
from django.contrib.auth.models import User
from .forms import CreateTeam, AddUserToTeam, CreateBoard
from .crud_utils import *


# Create your views here.

def index(request):
    # TODO creare colore random di backround quando si crea un team
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login")

    user_teams = TeamMember.objects.filter(user_username=request.user)

    teams = [Team.objects.get(pk=team.team_name) for team in user_teams]
    form = CreateTeam()

    if request.method == "POST":
        form = CreateTeam(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect("/project/")

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

        return HttpResponseRedirect("/project/")

    return render(request, "project/index.html", {"teams": teams, "form": form})


def team_details(request, team_name):
    user_form = AddUserToTeam()
    board_form = CreateBoard()

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
    if not request.user.is_authenticated or not TeamMember.objects.filter(team_name=team,
                                                                          user_username=request.user).exists():
        return HttpResponseRedirect("/project")

    user_admin = TeamMember.objects.get(team_name=team, user_username=request.user)

    if request.method == "POST":
        if request.POST.get("new_board"):
            board_form = CreateTeam(request.POST)

            if not board_form.is_valid():
                return HttpResponseRedirect("/project/%s" % team.name)

            board_name = board_form.cleaned_data["name"]
            board_description = board_form.cleaned_data["description"]
            create_board(board_name, board_description, team)

        elif request.POST.get("delete_board"):
            board_name = request.POST.get("delete_board")
            Board.objects.filter(name=board_name, team_name=team).delete()

        elif request.POST.get("delete_team"):
            Team.objects.filter(name=team.name).delete()

        elif request.POST.get("add_user_to_team"):
            user_form = AddUserToTeam(request.POST)

            if not user_form.is_valid():
                return HttpResponseRedirect("/project/%s" % team.name)

            username = user_form.cleaned_data["username"]
            role = user_form.cleaned_data["role"]

            try:
                u = User.objects.get(username=username)
            except User.DoesNotExist:
                print("l'utente non esiste")
                return HttpResponseRedirect("/project/%s" % team.name)

            user_already_exist = (
                    len(TeamMember.objects.filter(team_name=team, user_username=u)) > 0
            )

            if user_already_exist:
                print("l'utente è già nel team")
            else:
                tm = TeamMember(team_name=team, user_username=u, role=role)
                tm.save()

        elif request.POST.get("remove_user_from_team"):
            # TODO gestire opzioni varie (refactorare codice e pagina, un utente non admin non può ne aggiungere ne rimuovere partecipanti)
            username = request.POST.get("remove_user_from_team")
            user = User.objects.get(username=username)

            if user != request.user:
                TeamMember.objects.filter(user_username=user, team_name=team).delete()

        return HttpResponseRedirect("/project/%s" % team.name)

    return render(request, "project/team_details.html",
                  {"team": team, "boards": boards, "members": members, "user_admin": user_admin, "user_form": user_form,
                   "board_form": board_form})


def board_details(request, team_name, board_name):


    try:
        team = Team.objects.get(pk=team_name)
    except Team.DoesNotExist:
        return HttpResponseRedirect("/project")

    user_admin = TeamMember.objects.get(team_name=team, user_username=request.user)

    try:
        board = Board.objects.get(team_name=team, name=board_name)
    except Board.DoesNotExist:
        return HttpResponseRedirect("/project/%s" % team_name)

    board_form = CreateBoard(initial={"name": board.name, "description":board.description})

    # Se l'utente corrente non è nel team selezionato reindirizza a pagina dei suoi team
    if not request.user.is_authenticated or not TeamMember.objects.filter(team_name=team,
                                                                          user_username=request.user).exists():
        return HttpResponseRedirect("/project")
    try:
        columns = Column.objects.filter(team_name=team, board_name=board, status="p")
    except Column.DoesNotExist:
        pass

    try:
        tiles = Tile.objects.filter(team_name=team, board_name=board)
    except Tile.DoesNotExist:
        pass

    if request.method == "POST":

        if request.POST.get("edit_board"):
            board_form = CreateTeam(request.POST)

            if not board_form.is_valid():
                return HttpResponseRedirect(f"/project/{team_name}/{board_name}")

            new_board_name = board_form.cleaned_data["name"]
            new_board_description = board_form.cleaned_data["description"]
            n = edit_board(board_name, new_board_name, new_board_description, team)

            return HttpResponseRedirect(f"/project/{team_name}/{n}")

        elif request.POST.get("create_column"):
            column_title = request.POST.get("column_title")
            create_column(column_title, board, team)

        elif request.POST.get("delete_column"):
            column_id = request.POST.get("delete_column")
            delete_column(column_id)

        elif request.POST.get("change_column_status_archived"):
            column_id = request.POST.get("change_column_status_archived")
            change_column_status(column_id, "a")

        elif request.POST.get("add_new_tile"):
            tile_title = request.POST.get("tile_title")
            column_id = request.POST.get("add_new_tile")
            column = Column.objects.get(pk=column_id)

            create_tile(tile_title, "", "", "", request.user, column, board, team)
            # create_tile(title, content_type, content, multimedia_obj, request.user, column, board, team)

        elif request.POST.get("delete_tile"):
            tile_id = request.POST.get("delete_tile")
            delete_tile(tile_id)

        return HttpResponseRedirect(f"/project/{team_name}/{board_name}")

    return render(request, "project/board_details.html",
                  {"team": team, "board": board, "columns": columns, "tiles": tiles, "board_form": board_form,
                   "user_admin": user_admin})


def view_profile(request):
    return render(request, "project/view_profile.html", {})


def view_board_archive(request, team_name, board_name):
    # TODO se l'archivio è vuoto da frntend mostrare un messaggio che dice "archivio vuoto"

    try:
        team = Team.objects.get(pk=team_name)
    except Team.DoesNotExist:
        return HttpResponseRedirect("/project")
    try:
        board = Board.objects.get(team_name=team, name=board_name)
    except Board.DoesNotExist:
        return HttpResponseRedirect("/project/%s" % team_name)

    # Se l'utente corrente non è nel team selezionato reindirizza a pagina dei suoi team
    if not request.user.is_authenticated or not TeamMember.objects.filter(team_name=team,
                                                                          user_username=request.user).exists():
        return HttpResponseRedirect("/project")
    try:
        columns = Column.objects.filter(team_name=team, board_name=board, status="a")
    except Column.DoesNotExist:
        pass

    try:
        tiles = Tile.objects.filter(team_name=team, board_name=board)
    except Tile.DoesNotExist:
        pass

    if request.method == "POST":
        if request.POST.get("change_column_status_in_progress"):
            column_id = request.POST.get("change_column_status_in_progress")
            change_column_status(column_id, "p")

    return render(request, "project/board_archive.html",
                  {"team": team, "board": board, "columns": columns, "tiles": tiles})
