from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    ROLE_OPTIONS = (
        ("a", "admin"),
        ("m", "member")
    )
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    user_username = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLE_OPTIONS)


class Board(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Column(models.Model):
    STATUS_OPTIONS = (
        ("p", "in_progress"),
        ("a", "archived")
    )

    # id_col = models.IntegerField(unique=True)
    title = models.CharField(max_length=45)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    board_name = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Tile(models.Model):
    CONTENT_OPTIONS = (
        ("o", "org"),
        ("i", "inf")
    )

    title = models.CharField(max_length=45)
    creation_date = models.DateTimeField(default=timezone.now)
    content_type = models.CharField(max_length=1, choices=CONTENT_OPTIONS)
    content = models.TextField()
    multimedia_obj = models.CharField(max_length=45)

    column_title = models.ForeignKey(Column, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    board_name = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
