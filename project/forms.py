from django import forms


class CreateTeam(forms.Form):
    name = forms.CharField(label="Nome", max_length=30)
    description = forms.CharField(label="Descrizione", max_length=255, required=False)


# class CreateTile(forms.Form):
#     CONTENT_OPTIONS = (
#         ("o", "org"),
#         ("i", "inf")
#     )
#
#     title = forms.CharField(label="Titolo", max_length=45)
#     # creation_date = forms.DateTimeField(default=timezone.now)
#     content_type = forms.CharField(label="Tipo contenuto", max_length=1, choices=CONTENT_OPTIONS)
#     content = forms.CharField(label="Contenuto", max_length=255)
#     multimedia_obj = forms.CharField(label="Immagine", max_length=45)

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
