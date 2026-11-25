from django.db import models


class Diretor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=150)
    sinopse = models.TextField()
    ano_lancamento = models.IntegerField()
    duracao = models.IntegerField()

    diretor = models.ForeignKey(
        Diretor,
        on_delete=models.CASCADE,
        related_name='filmes'
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='filmes'
    )

    def __str__(self):
        return self.titulo