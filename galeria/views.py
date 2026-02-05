from django.shortcuts import render
from galeria.models import Fotografia


def index(request):
    """Função responsável por responder a uma requisção que leva a página principal do site"""

    # item do banco de dados
    fotografias = Fotografia.objects.all()

    return render(request, "galeria/index.html", {"cards": fotografias})


def imagem(request):
    return render(request, "galeria/imagem.html")
