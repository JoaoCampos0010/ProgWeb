from django.db import models
from django.contrib.auth.models import User



# Classe para armazenar status e cores correspondentes pra exibir no template
class Status(models.Model):
    ordem = models.PositiveSmallIntegerField(unique=True)
    nome = models.CharField(max_length=50)
    cor = models.CharField(max_length=7, help_text="Cor em formato hexadecimal, ex: #FF0000")

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['ordem']

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

    def __str__(self):
        return self.nome


class Caixa(models.Model):
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(null=True, blank=True)
    valor_inicial = models.DecimalField(decimal_places=2, max_digits=7)
    valor_final = models.DecimalField(decimal_places=2, max_digits=7, null=True, blank=True)

    def __str__(self):
        if(self.data_fechamento):
            return f"Caixa {self.pk} - {self.data_abertura} (Fechado)"
        else:
            return f"Caixa {self.pk} - {self.data_abertura} (Aberto)"
        
    class Meta:
        ordering = ['-data_abertura']

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(verbose_name="preço", max_digits=7, decimal_places=2)
    descricao = models.CharField(max_length=255)
    estoque = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} - R${self.preco}"


class Pedido(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    cliente = models.CharField(max_length=255)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, default=1)
    valor_total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.PROTECT)

    def __str__(self):
        return f"Pedido {self.pk} - {self.cliente} ({self.status})"


class Itens(models.Model):
    quantidade = models.PositiveSmallIntegerField(default=1)
    valor_item = models.DecimalField(decimal_places=2, max_digits=7)
    observacao = models.CharField(max_length=255, null=True, blank=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if(self.pedido):
            return f"Item {self.pk} - {self.quantidade} x {self.produto.nome} ({self.pedido.pk})"
        else:
            return f"Item {self.pk} - {self.quantidade} x {self.produto.nome} (Sem Pedido)"
