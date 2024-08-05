from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # Usuário personalizado (se precisar adicionar campos extras)
    pass

class Livro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    ano_publicacao = models.IntegerField()

    def __str__(self):
        return self.titulo

