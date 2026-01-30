from django.shortcuts import render


def index(request):
    """Função responsável por responder a uma requisção"""
    return render(request, "index.html")
