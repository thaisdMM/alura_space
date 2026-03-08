from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import auth

from django.contrib import messages

from usuarios.forms import LoginForms, CadastroForms

# Definindo a classe de usuário de forma dinâmica
User = get_user_model()


def login(request):
    # instanciação de objeto formulario
    login_form = LoginForms()

    if request.method == "POST":
        login_form = LoginForms(request.POST)

        if login_form.is_valid():

            # # cleaned_data para maior segurança e tipagem -
            # valida os dados e converte para tipos python
            dados = login_form.cleaned_data

            nome = dados.get("nome_login")
            senha = dados.get("senha")

            # usar método do django para autenticação
            usuario = auth.authenticate(request, username=nome, password=senha)

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"{nome} logado com sucesso!")
                return redirect("index")
            else:
                messages.error(request, "Erro ao efetuar login.")
                return redirect("login")

    # Contexto para template compartilhado,
    # já que mudei o html para form_auth - para ser usado tanto para login quanto para cadastro
    context = {
        "form": login_form,
        "page_title": "Login - Alura Space",
        "form_title": "Faça o seu login",
        "button_text": "Entrar",
        "footer_message": "Não tem uma conta?",
        "footer_link": "cadastro",  # nome da url
        "footer_link_text": "Cadastre-se aqui",
    }
    return render(request, "usuarios/form_auth.html", context)


def cadastro(request):
    cadastro_form = CadastroForms()

    if request.method == "POST":
        cadastro_form = CadastroForms(request.POST)

        if cadastro_form.is_valid():

            # # cleaned_data para maior segurança e tipagem -
            # valida os dados e converte para tipos python
            dados = cadastro_form.cleaned_data

            nome = dados.get("nome_cadastro")
            email = dados.get("email")
            senha = dados.get("senha_1")

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já cadastrado no sistema.")
                return redirect("cadastro")

            User.objects.create_user(username=nome, email=email, password=senha)
            messages.success(request, "Cadastro efetuado com sucesso!")
            return redirect("login")

    context = {
        "form": cadastro_form,
        "page_title": "Cadastro - Alura Space",
        "form_title": "Crie sua conta",
        "button_text": "Cadastrar",
        "footer_message": "Já tem uma conta?",
        "footer_link": "login",
        "footer_link_text": "Faça login aqui",
    }
    return render(request, "usuarios/form_auth.html", context)


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect("login")
