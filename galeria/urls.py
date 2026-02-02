from django.urls import path
from galeria.views import index, imagem

# criou para incluir todos os paths - rotas de galeria
urlpatterns = [path("", index), path("imagem/", imagem)]
