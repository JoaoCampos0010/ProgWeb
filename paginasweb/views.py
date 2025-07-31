from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria, Produto, Pedido, Itens, Caixa, FormaPagamento
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'paginasweb/index.html'
    login_url = 'Login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produto_count'] = Produto.objects.count()
        context['pedido_count'] = Pedido.objects.count()
        return context

class SobreView(LoginRequiredMixin, TemplateView):
    template_name = 'paginasweb/sobre.html'
    login_url = 'Login'

# CREATE
class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Categoria', 'botao': 'Cadastrar'}

class ProdutoCreate(LoginRequiredMixin, CreateView):
    model = Produto
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'preco', 'descricao', 'estoque', 'categoria']
    success_url = reverse_lazy('index')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Produto', 'botao': 'Cadastrar'}

class PedidoCreate(LoginRequiredMixin, CreateView):
    model = Pedido
    template_name = 'paginasweb/form.html'
    fields = ['cliente', 'status', 'valor_total', 'forma_pagamento']
    success_url = reverse_lazy('index')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Pedido', 'botao': 'Cadastrar'}

class ItensCreate(LoginRequiredMixin, CreateView):
    model = Itens
    template_name = 'paginasweb/form.html'
    fields = ['quantidade', 'valor_item', 'observacao', 'produto', 'pedido']
    success_url = reverse_lazy('index')
    login_url = 'Login'
    extra_context = {'titulo': 'Adicionar Item ao Pedido', 'botao': 'Adicionar'}

class CaixaCreate(LoginRequiredMixin, CreateView):
    model = Caixa
    template_name = 'paginasweb/form.html'
    fields = ['valor_inicial', 'valor_final']
    success_url = reverse_lazy('index')
    login_url = 'Login'
    extra_context = {'titulo': 'Abrir Caixa', 'botao': 'Abrir'}

class FormaPagamentoCreate(LoginRequiredMixin, CreateView):
    model = FormaPagamento
    template_name = 'paginasweb/form.html'
    fields = ['tipo']
    success_url = reverse_lazy('index')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Forma de Pagamento', 'botao': 'Cadastrar'}
