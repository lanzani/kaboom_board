from django.shortcuts import render, redirect
from .forms import UserRegisterForm


# Create your views here.
def register(response):
    # todo controllare se esiste già l'utente
    if response.method == "POST":
        form = UserRegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("project:index")
    else:
        form = UserRegisterForm()

    return render(response, "user_register/register.html", {"form": form})
