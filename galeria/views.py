from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from galeria.models import Fotografia


def index(request):
    """
    Função responsável por responder a uma requisção que leva a página principal do site
    Só usuários autenticados tem acesso ao index.
    """

    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect("login")

    # ordem decrescente - mais nova primeiro
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    context = {
        "cards": fotografias,
        "page_title": "Galeria de fotografias do espaço!",
    }

    return render(request, "galeria/gallery_list.html", context)


def imagem(request, foto_id):

    #  Passa o model, e do objeto a pk(primary_key)= foto_id
    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    # esse dicionario é para passar para o imagem.html o objeto que faz referencia ao id
    return render(request, "galeria/imagem.html", {"fotografia": fotografia})


def buscar(request):
    """
    Função responsável por possibilitar a busca de uma imagem por nome(nome_a_buscar)
    ou pela categoria(categoria__icontains).

    Só usuários autenticados tem acesso.
    """

    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect("login")

    # buscar todos os objetos que tem no banco de dados
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        # request.GET['buscar'] - dentro do input do _header.html o name="buscar"
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar:

            from django.db.models import Q

            # nome__icontains - se ao menos parte faz referência ao nome que esta buscando
            # Q - Q objects permitem fazer buscas complexas (OR, AND, NOT).
            fotografias = fotografias.filter(
                Q(nome__icontains=nome_a_buscar) | Q(categoria__icontains=nome_a_buscar)
            )

    context = {"cards": fotografias, "page_title": "Resultados da busca"}

    return render(request, "galeria/gallery_list.html", context)
