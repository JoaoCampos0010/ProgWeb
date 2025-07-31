from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class FormaPagamento(models.Model):
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo
    


class Gerente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='gerente')

    

class Caixa(models.Model):
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(auto_now=True)
    valor_inicial = models.DecimalField(decimal_places=2, max_digits=7)
    valor_final = models.DecimalField(decimal_places=2, max_digits=7)

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(verbose_name="preço", max_digits=7, decimal_places=2)
    descricao = models.CharField(max_length=255)
    estoque = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    cliente = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    valor_total = models.DecimalField(decimal_places=2, max_digits=7)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.PROTECT)

class Itens(models.Model):
    quantidade = models.PositiveSmallIntegerField(default=1)
    valor_item = models.DecimalField(decimal_places=2, max_digits=7)
    observacao = models.CharField(max_length=255)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
