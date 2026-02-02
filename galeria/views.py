from django.shortcuts import render


def index(request):
    """Função responsável por responder a uma requisção"""
    return render(request, "galeria/index.html")


def imagem(request):
    return render(request, "galeria/imagem.html")
