from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

 
def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect("index2")

    form = AuthenticationForm()
    return render(request, "acceder.html", {"form": form})

class VistaRegistro(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro.html", {"form": form})

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get("username")
            login(request, usuario)
            return redirect("index2")
        else:
            
            return render(request, "registro.html", {"form": form})


def salir(request):
    logout(request)
    messages.success(request, F"Tu sesión se ha cerrado correctamente")
    return redirect("index")
