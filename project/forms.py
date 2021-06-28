from django import forms


class CreateTeam(forms.Form):
    name = forms.CharField(label="Nome", max_length=30)
    description = forms.CharField(label="Descrizione", max_length=255, required=False)

