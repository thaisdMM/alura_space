from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from galeria.models import Fotografia


def index(request):
    """Função responsável por responder a uma requisção que leva a página principal do site"""

    # agora que criamos login, cadastro e logout,
    # vamos alterar a view de galeria para só acessar o index pessoas autenticadas
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect("login")

    # item do banco de dados - vai filtrar pelas imagens publicadas
    # -data_fotografia = com o '-' ordem decrescente: mais nova primeiro
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    return render(request, "galeria/index.html", {"cards": fotografias})


# vai receber o foto_id para fazer referencia ao id do banco de dados
def imagem(request, foto_id):

    #  Passa o model, e do objeto a pk(primary_key)= foto_id
    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    # esse dicionario é para passar para o imagem.html o objeto que faz referencia ao id
    return render(request, "galeria/imagem.html", {"fotografia": fotografia})


def buscar(request):

    # agora que criamos login, cadastro e logout,
    # vamos alterar a view de galeria para só acessar conseguir buscar pessoas autenticadas
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect("login")
    # buscar todos os objetos que tem no banco de dados
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    if "buscar" in request.GET:
        # request.GET['buscar'] - dentro do input do _menu.html o name="buscar"
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar:
            # nome__icontains - se ao menos parte faz referência ao nome que esta buscando
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, "galeria/buscar.html", {"cards": fotografias})
