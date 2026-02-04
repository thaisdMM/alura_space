from django.db import models

# criar classes para virar tabela de banco de dados(sqlite3) usando Django ORM
#  1- usar um comando no terminal para criar migrations : python manage.py makemigrations
# 2- usar um comando no terminal para rodar migrations : ppython manage.py migrate


class Fotografia(models.Model):
    # Charfiel - str caracteres
    # blank = evita str vazia
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    # nome da foto
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"
