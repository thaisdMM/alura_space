from django.urls import path
from galeria.views import index, imagem

# criou para incluir todos os paths - rotas de galeria
urlpatterns = [
    path("", index, name="index"),
    # /<int:foto_id>: acrescentou para exibir outras fotos pelo id
    path("imagem/<int:foto_id>", imagem, name="imagem"),
]
