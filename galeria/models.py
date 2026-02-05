from django.db import models

# criar classes para virar tabela de banco de dados(sqlite3) usando Django ORM

# TODA VEZ QUE MUDA O MODELS TEM QUE:
#  1- usar um comando no terminal para criar migrations : python manage.py makemigrations
# 2- usar um comando no terminal para rodar migrations : ppython manage.py migrate


class Fotografia(models.Model):
    """
    Esta classe representa uma tabela no banco de dados.
    Cada atributo da classe vira uma coluna na tabela.
    """

    # Como é Charfield tem ser tupla
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]

    # Campo de texto curto (VARCHAR no banco)
    # max_length:
    #   - É uma regra REAL de banco de dados
    #   - O banco NÃO aceita mais caracteres do que isso
    #
    # null=False:
    #   - O banco NÃO aceita NULL
    #   - Mas aceita string vazia ("")
    #
    # blank=False:
    #   - NÃO é regra de banco
    #   - Só é usada em formulários (ModelForm, Admin)
    #   - NÃO é aplicada automaticamente no shell ou em .save()
    nome = models.CharField(max_length=100, null=False, blank=False)

    # Mesmo comportamento do campo "nome"
    legenda = models.CharField(max_length=150, null=False, blank=False)

    # definir as categorias que serão opções para não poder criar aleatório
    # precisa definir padrão default - nesse caso esta vazio, mas nunca será vazio pois tem acima OPCOES_CATEGORIA
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default="")

    # TextField:
    # - Usado para textos longos
    # - NÃO tem limite máximo no banco (por isso não aparece max_length na migration)
    #
    # IMPORTANTE:
    # null=False:
    #   - Impede NULL no banco
    #
    # blank=False:
    #   - Impede string vazia APENAS em formulários
    #   - NÃO impede string vazia ao usar o shell ou .save()
    #
    # Por isso este campo pode acabar salvo como "" se não houver validação
    descricao = models.TextField(null=False, blank=False)

    # Nome do arquivo da foto (string simples)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        # Método usado apenas para representação textual
        # Não tem impacto no banco nem na validação
        return f"Fotografia [nome={self.nome}]"
