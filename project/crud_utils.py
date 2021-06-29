from .models import Team, TeamMember, Board, Column, Tile

# TODO Team

# TODO Board


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


def change_column_status(column_id, status):
    c = Column.objects.get(pk=column_id)
    c.status = status
    c.save()


# Tile


def delete_tile(tile_id):
    Tile.objects.get(pk=tile_id).delete()