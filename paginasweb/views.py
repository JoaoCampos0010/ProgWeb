from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
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
    success_url = reverse_lazy('listar_categoria')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Categoria', 'botao': 'Cadastrar'}

class ProdutoCreate(LoginRequiredMixin, CreateView):
    model = Produto
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'preco', 'descricao', 'estoque', 'categoria']
    success_url = reverse_lazy('listar_produto')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Produto', 'botao': 'Cadastrar'}

class PedidoCreate(LoginRequiredMixin, CreateView):
    model = Pedido
    template_name = 'paginasweb/form.html'
    fields = ['cliente', 'status', 'valor_total', 'forma_pagamento']
    success_url = reverse_lazy('listar_pedido')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Pedido', 'botao': 'Cadastrar'}

class ItensCreate(LoginRequiredMixin, CreateView):
    model = Itens
    template_name = 'paginasweb/form.html'
    fields = ['quantidade', 'valor_item', 'observacao', 'produto', 'pedido']
    success_url = reverse_lazy('listar_itens')
    login_url = 'Login'
    extra_context = {'titulo': 'Adicionar Item ao Pedido', 'botao': 'Adicionar'}

class CaixaCreate(LoginRequiredMixin, CreateView):
    model = Caixa
    template_name = 'paginasweb/form.html'
    fields = ['valor_inicial', 'valor_final']
    success_url = reverse_lazy('listar_caixa')
    login_url = 'Login'
    extra_context = {'titulo': 'Abrir Caixa', 'botao': 'Abrir'}

class FormaPagamentoCreate(LoginRequiredMixin, CreateView):
    model = FormaPagamento
    template_name = 'paginasweb/form.html'
    fields = ['tipo']
    success_url = reverse_lazy('listar_forma_pagamento')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Forma de Pagamento', 'botao': 'Cadastrar'}





#Update 

class CategoriaUpdate(LoginRequiredMixin,  UpdateView):
    model = Categoria
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('listar_categoria')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Categoria', 'botao': 'Cadastrar'}

class ProdutoUpdate(LoginRequiredMixin,  UpdateView):
    model = Produto
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'preco', 'descricao', 'estoque', 'categoria']
    success_url = reverse_lazy('listar_produto')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Produto', 'botao': 'Cadastrar'}

class PedidoUpdate(LoginRequiredMixin,  UpdateView):
    model = Pedido
    template_name = 'paginasweb/form.html'
    fields = ['cliente', 'status', 'valor_total', 'forma_pagamento']
    success_url = reverse_lazy('listar_pedido')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Pedido', 'botao': 'Cadastrar'}

class ItensUpdate(LoginRequiredMixin,  UpdateView):
    model = Itens
    template_name = 'paginasweb/form.html'
    fields = ['quantidade', 'valor_item', 'observacao', 'produto', 'pedido']
    success_url = reverse_lazy('listar_itens')
    login_url = 'Login'
    extra_context = {'titulo': 'Adicionar Item ao Pedido', 'botao': 'Adicionar'}

class CaixaUpdate(LoginRequiredMixin,   UpdateView):
    model = Caixa
    template_name = 'paginasweb/form.html'
    fields = ['valor_inicial', 'valor_final']
    success_url = reverse_lazy('listar_caixa')
    login_url = 'Login'
    extra_context = {'titulo': 'Abrir Caixa', 'botao': 'Abrir'}

class FormaPagamentoUpdate(LoginRequiredMixin,   UpdateView):
    model = FormaPagamento
    template_name = 'paginasweb/form.html'
    fields = ['tipo']
    success_url = reverse_lazy('listar_forma_pagamento')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Forma de Pagamento', 'botao': 'Cadastrar'}




#Delete

class CategoriaDelete( DeleteView):
    model = Categoria
    template_name = 'paginasweb/form-excluir.html'
    success_url = reverse_lazy('listar_categoria')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Categoria', 'botao': 'Cadastrar'}

class ProdutoDelete( DeleteView):
    model = Produto
    template_name = 'paginasweb/form-excluir.html'
    success_url = reverse_lazy('listar_produto')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Produto', 'botao': 'Cadastrar'}

class PedidoDelete( DeleteView):
    model = Pedido
    template_name = 'paginasweb/form-excluir.html'
    success_url = reverse_lazy('listar_pedido')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Pedido', 'botao': 'Cadastrar'}

class ItensDelete( DeleteView):
    model = Itens
    template_name = 'paginasweb/form-excluir.html'
    success_url = reverse_lazy('listar_itens')
    login_url = 'Login'
    extra_context = {'titulo': 'Adicionar Item ao Pedido', 'botao': 'Adicionar'}

class CaixaDelete( DeleteView):
    model = Caixa
    template_name = 'paginasweb/form-excluir.html'
    success_url = reverse_lazy('listar_caixa')
    login_url = 'Login'
    extra_context = {'titulo': 'Abrir Caixa', 'botao': 'Abrir'}

class FormaPagamentoDelete( DeleteView):
    model = FormaPagamento
    template_name = 'paginasweb/form-excluir.html'
    success_url = reverse_lazy('listar_forma_pagamento')
    login_url = 'Login'
    extra_context = {'titulo': 'Cadastrar Forma de Pagamento', 'botao': 'Cadastrar'}




#List

class CategoriaList( ListView):
    model = Categoria
    template_name = 'paginasweb/listar_categorias.html'
    success_url = reverse_lazy('index')

class ProdutoList( ListView):
    model = Produto
    template_name = 'paginasweb/listar_produto.html'
    success_url = reverse_lazy('index')

class PedidoList( ListView):
    model = Pedido
    template_name = 'paginasweb/listar_pedido.html'
    success_url = reverse_lazy('index')

class ItensList( ListView):
    model = Itens
    template_name = 'paginasweb/listar_itens.html'
    success_url = reverse_lazy('index')

class CaixaList( ListView):
    model = Caixa
    template_name = 'paginasweb/listar_caixa.html'
    success_url = reverse_lazy('index')

class FormaPagamentoList( ListView):
    model = FormaPagamento
    template_name = 'paginasweb/listar_forma_pagamento.html'
    success_url = reverse_lazy('index')

