from django.db import models

class Contato(models.Model):

    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.EmailField()
    noticias = models.BooleanField()
    mensagem = models.TextField()

    def __str__(self):
        return self.nome
    