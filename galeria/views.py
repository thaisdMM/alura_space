from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia


def index(request):
    """Função responsável por responder a uma requisção que leva a página principal do site"""

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
