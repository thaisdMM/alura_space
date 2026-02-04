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


# CODIGO NO TERMINAL PARA CRIAR UMA FOTO

# (.venv) ➜  alura-space git:(persistencia-dados-e-admin) python manage.py shell
# 13 objects imported automatically (use -v 2 for details).

# Cmd click to launch VS Code Native REPL
# Python 3.13.5 (main, Jun 11 2025, 15:36:57) [Clang 17.0.0 (clang-1700.0.13.3)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from galeria.models import Fotografia
# >>> foto = Fotografia(nome="Nebulosa de Carina", legenda="webbtelecope.org / NASA / James Webb", foto="carina-nebulosa.png")
# >>> foto.save()
# >>> Fotografia.objects.all()
# <QuerySet [<Fotografia: Fotografia [nome=Nebulosa de Carina]>]>
# >>>
