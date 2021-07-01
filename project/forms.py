from django import forms
from django.contrib.auth.models import User

from .models import Tile


class CreateTeam(forms.Form):
    name = forms.CharField(label="Nome", max_length=30)
    description = forms.CharField(label="Descrizione", max_length=255, required=False)


class CreateTileText(forms.Form):

    def __init__(self, author, *args, **kwargs):
        super(CreateTileText, self).__init__(*args, **kwargs)
        self.fields["author"].choices = author

    CONTENT_OPTIONS = (
        ("o", "Organizzativo"),
        ("i", "Informativo")
    )

    title = forms.CharField(label="Titolo", max_length=45)
    content = forms.CharField(label="Contenuto", widget=forms.Textarea)
    content_type = forms.ChoiceField(label='Tipologia messaggio', choices=CONTENT_OPTIONS, widget=forms.RadioSelect)
    author = forms.ChoiceField(label="Autore", choices=(), required=True)


class CreateTileMul(forms.Form):

    def __init__(self, author, *args, **kwargs):
        super(CreateTileMul, self).__init__(*args, **kwargs)
        self.fields["author"].choices = author

    CONTENT_OPTIONS = (
        ("o", "Organizzativo"),
        ("i", "Informativo")
    )

    title = forms.CharField(label="Titolo", max_length=45)
    multimedia_obj = forms.ImageField(label="Immagine")
    content_type = forms.ChoiceField(label='Tipologia messaggio', choices=CONTENT_OPTIONS, widget=forms.RadioSelect)
    author = forms.ChoiceField(label="Autore", choices=(), required=True)


# class CreateTileMul(forms.ModelForm):
#
#     def __init__(self, author, *args, **kwargs):
#
#         super(CreateTileMul, self).__init__(*args, **kwargs)
#         self.fields["author"].choices = author
#
#     author = forms.ChoiceField(label="Autore", choices=(), required=True)
#     class Meta:
#         model = Tile
#         fields = ("title", "content_type", "multimedia_obj", "author")
#
# class CreateTileText(forms.ModelForm):
#     author = forms.ChoiceField(label='Author', choices=())
#     class Meta:
#         model = Tile
#         fields = ("title", "content_type", "content", "author")


class AddUserToTeam(forms.Form):
    ROLE_OPTIONS = (
        ("a", "admin"),
        ("m", "member")
    )
    username = forms.CharField(label="Username", max_length=30)
    role = forms.ChoiceField(label='Ruolo', choices=ROLE_OPTIONS, widget=forms.RadioSelect)


class CreateBoard(forms.Form):
    name = forms.CharField(label="Nome", max_length=45)
    description = forms.CharField(label="Descrizione", max_length=255, required=False)


class CreateColumn(forms.Form):
    title = forms.CharField(label="Titolo", max_length=45)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', "first_name", "last_name"]
