from datetime import date

from .models import Team, TeamMember, Board, Column, Tile


# todo refactor, rivedere come organizzare i metodi e il passaggio dei parametri

# TODO Team

# Board
def create_board(name, description, team):
    board_already_exist = (
            len(Board.objects.filter(name=name, team_name=team)) > 0
    )

    if board_already_exist:
        print("La board è già nel team")
    else:
        b = Board(name=name, description=description, team_name=team)
        b.save()


def edit_board(old_name, new_name, new_description, team):
    board_already_exist = False

    if old_name != new_name:
        board_already_exist = (
                len(Board.objects.filter(name=new_name, team_name=team)) > 0
        )

    if board_already_exist:
        print("La board è già nel team")
        return old_name
    else:
        b = Board.objects.get(name=old_name, team_name=team)

        b.name = new_name
        b.description = new_description

        b.save()
        return new_name


# Column
def create_column(column_title, board, team):
    column_already_exist = (
            len(Column.objects.filter(title=column_title, board_name=board, team_name=team)) > 0
    )

    if column_already_exist:
        print(f"[INVALID] La colonna {column_title} esiste già")
    elif 45 >= len(column_title) > 0:
        c = Column(title=column_title, board_name=board, team_name=team, status="p")
        c.save()
    else:
        print("[INVALID] Il nome può essere lungo max 45 caratteri")


def delete_column(column_id):
    c = Column.objects.get(pk=column_id)

    if c.status == "a":
        print("[INVALID] Impossibile eliminare le colonne archiviate")
    else:
        c.delete()


def edit_column(old_title, new_title, board, team):
    column_already_exist = False

    if old_title != new_title:
        column_already_exist = (
                len(Column.objects.filter(title=new_title, board_name=board, team_name=team)) > 0
        )

    if column_already_exist:
        print("La board è già nel team")
    else:
        c = Column.objects.get(title=old_title, board_name=board, team_name=team)
        c.title = new_title
        c.save()


def change_column_status(column_id, status):
    c = Column.objects.get(pk=column_id)
    c.status = status
    c.save()


# Tile

def create_tile(title, content_type, content, multimedia_obj, author, column, board, team):
    t = Tile(title=title, content_type=content_type, content=content, multimedia_obj=multimedia_obj,
             creation_date=date.today(), author=author, column_title=column, team_name=team, board_name=board)

    t.save()


def edit_txt_tile(tile_id, title, content, content_type):
    t = Tile.objects.get(pk=tile_id)

    if title != "":
        t.title = title

    if content_type != "":
        t.content_type = content_type

    if content != "":
        t.content = content

    t.save()


def edit_mul_tile(tile_id, title, multimedia_obj, content_type):
    t = Tile.objects.get(pk=tile_id)

    if title != "":
        t.title = title

    if content_type != "":
        t.content_type = content_type

    if multimedia_obj != "":
        t.multimedia_obj = multimedia_obj

    t.save()


def delete_tile(tile_id):
    Tile.objects.get(pk=tile_id).delete()

# TODO User
