from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome=models.CharField(max_length=255)


class FormaPagamento(models.Model):
    tipo=models.CharField(max_length=255)


class Caixa(models.Model):
    data_abertura=models.DateTimeField(auto_now_add=True)
    data_fechamento=models.DateTimeField(auto_now=True)
    valor_inicial=models.DecimalField(decimal_places=2, max_digits=7)
    valor_final=models.DecimalField(decimal_places=2, max_digits=7)


class Produto(models.Model):
    nome=models.CharField(max_length=255)
    preco=models.DecimalField(verbose_name="preço")
    descricao=models.CharField(max_length=255)
    estoque=models.PositiveIntegerField()
    categoria=models.ForeignKey(Categoria, on_delete=models.PROTECT)


class Pedido(models.Model):
    data_hora=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=255)
    valor_total=models.DecimalField(decimal_places=2, max_digits=7)
    forma_pagamento=FormaPagamento()
    

class Itens(models.Model):
    quantidade=models.PositiveSmallIntegerField(default=1)
    valor_item=models.DecimalField(decimal_places=2, max_digits=7)
    observacao=models.CharField(max_length=255)
    produto=Produto()
    pedido=Pedido()
