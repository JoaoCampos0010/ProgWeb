from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria, Produto, Pedido, Itens, Caixa, FormaPagamento

from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(TemplateView):
    template_name = 'paginasweb/index.html'

class SobreView(TemplateView):
    template_name = 'paginasweb/sobre.html'


# ----------------------------- CREATE VIEWS -----------------------------
class CategoriaCreate(CreateView):
    model = Categoria
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Cadastrar Categoria', 'botao': 'Cadastrar'}

class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'preco', 'descricao', 'estoque', 'categoria']
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Cadastrar Produto', 'botao': 'Cadastrar'}

class PedidoCreate(CreateView):
    model = Pedido
    template_name = 'paginasweb/form.html'
    fields = ['cliente', 'status', 'valor_total', 'forma_pagamento']
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Cadastrar Pedido', 'botao': 'Cadastrar'}

class ItensCreate(CreateView):
    model = Itens
    template_name = 'paginasweb/form.html'
    fields = ['quantidade', 'valor_item', 'observacao', 'produto', 'pedido']
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Adicionar Item ao Pedido', 'botao': 'Adicionar'}

class CaixaCreate(CreateView):
    model = Caixa
    template_name = 'paginasweb/form.html'
    fields = ['valor_inicial', 'valor_final']
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Abrir Caixa', 'botao': 'Abrir'}

class FormaPagamentoCreate(CreateView):
    model = FormaPagamento
    template_name = 'paginasweb/form.html'
    fields = ['tipo']
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Cadastrar Forma de Pagamento', 'botao': 'Cadastrar'}

# ----------------------------- UPDATE VIEWS -----------------------------
class CategoriaUpdate(UpdateView):
    model = Categoria
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Editar Categoria', 'botao': 'Salvar'}

class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'preco', 'descricao', 'estoque', 'categoria']
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Editar Produto', 'botao': 'Salvar'}

class PedidoUpdate(UpdateView):
    model = Pedido
    template_name = 'paginasweb/form.html'
    fields = ['cliente', 'status', 'valor_total', 'forma_pagamento']
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Editar Pedido', 'botao': 'Salvar'}

class ItensUpdate(UpdateView):
    model = Itens
    template_name = 'paginasweb/form.html'
    fields = ['quantidade', 'valor_item', 'observacao', 'produto', 'pedido']
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Editar Item', 'botao': 'Salvar'}

class CaixaUpdate(UpdateView):
    model = Caixa
    template_name = 'paginasweb/form.html'
    fields = ['valor_inicial', 'valor_final']
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Editar Caixa', 'botao': 'Salvar'}

class FormaPagamentoUpdate(UpdateView):
    model = FormaPagamento
    template_name = 'paginasweb/form.html'
    fields = ['tipo']
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Editar Forma de Pagamento', 'botao': 'Salvar'}

# ----------------------------- DELETE VIEWS -----------------------------
class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Categoria', 'botao': 'Excluir'}

class ProdutoDelete(DeleteView):
    model = Produto
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Produto', 'botao': 'Excluir'}

class PedidoDelete(DeleteView):
    model = Pedido
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Pedido', 'botao': 'Excluir'}

class ItensDelete(DeleteView):
    model = Itens
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Item do Pedido', 'botao': 'Excluir'}

class CaixaDelete(DeleteView):
    model = Caixa
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Fechar Caixa', 'botao': 'Excluir'}

class FormaPagamentoDelete(DeleteView):
    model = FormaPagamento
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Forma de Pagamento', 'botao': 'Excluir'}
