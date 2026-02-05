from django.contrib import admin

from galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    """Classe para exibir e editar as fotografias no painel do Django Admin"""

    list_display = ("id", "nome", "legenda")
    # para exibir como link
    list_display_links = ("id", "nome")
    # adicionar um campo de busca
    # - search_fields tem que ser uma tupla só a , já é o suficiente ("nome",)
    search_fields = ("nome",)
    # filtrar por categoria
    list_filter = ("categoria",)
    # paginação do site
    list_per_page = 10


# toda vez que criar uma nova classe tem que passar para o admin.site.register
admin.site.register(Fotografia, ListandoFotografias)
