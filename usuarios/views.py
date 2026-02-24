from django.shortcuts import render, redirect

# forma mais recomendada do que:
#  from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.contrib import auth

from usuarios.forms import LoginForms, CadastroForms

# Definindo a classe de usuário de forma dinâmica
User = get_user_model()


def login(request):
    # instanciação de objeto formulario
    login_form = LoginForms()

    # Validação 1
    if request.method == "POST":
        login_form = LoginForms(request.POST)

        # validação 2
        if login_form.is_valid():

            # novamente diferente do professor vou usar o cleaned_data primeiro
            dados = login_form.cleaned_data

            # validação 3

            # usar o get() ao invés de login_form['nome_login'] - diferente professor

            nome = dados.get("nome_login")
            senha = dados.get("senha")

            # usar metodo do django para autenticação
            usuario = auth.authenticate(request, username=nome, password=senha)

            # validação
            if usuario is not None:
                auth.login(request, usuario)

                return redirect("index")
            else:
                return redirect("login")

    return render(request, "usuarios/login.html", {"form": login_form})


def cadastro(request):
    cadastro_form = CadastroForms()

    # validação 1
    # Para criar um cadastro novo
    if request.method == "POST":
        cadastro_form = CadastroForms(request.POST)

        # validação 2
        if cadastro_form.is_valid():

            #  diferente do professor
            # # cleaned_data para maior segurança e tipagem -
            # valida os dados e converte para tipos python

            dados = cadastro_form.cleaned_data

            # validação 3
            # se a senha for diferente vai redirecionar para fazer cadastro

            #  código do professor
            # if cadastro_form["senha_1"].value() != cadastro_form["senha_2"].value():

            # trocar pelo get() - para maior segurança contra erros
            # o get() não trava o sistema

            if dados.get("senha_1") != dados.get("senha_2"):
                return redirect("cadastro")

            # senha1 e 2 são iguais:
            # detalhe como o professor nao usava o get() nem o cleaned_data todos os dados estavam assim:
            # nome = cadastro_form["nome_cadastro"].value()
            nome = dados.get("nome_cadastro")
            email = dados.get("email")
            senha = dados.get("senha_1")

            # validação 4
            # ver se existe um usario com o mesmo nome
            if User.objects.filter(username=nome).exists():
                return redirect("cadastro")

            # criar um novo usuario
            User.objects.create_user(username=nome, email=email, password=senha)
            # não precisa usar o save() pois o create_user já salva automaticamente,
            # só se fizer mudança, ai tem que salvar - comentei o save() do codigo do professor
            # usuario.save()
            return redirect("login")

    return render(request, "usuarios/cadastro.html", {"form": cadastro_form})
