from django.shortcuts import render

from usuarios.forms import LoginForms, CadastroForms


def login(request):
    # instanciação de objeto formulario
    login_form = LoginForms()
    return render(request, "usuarios/login.html", {"form": login_form})


def cadastro(request):
    cadastro_form = CadastroForms()
    return render(request, "usuarios/cadastro.html", {"form": cadastro_form})
