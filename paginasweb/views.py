from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Categoria, Produto, Pedido, Itens, Caixa, FormaPagamento, Status
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'paginasweb/index.html'
    login_url = 'Login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produto_count'] = Produto.objects.count()
        context['pedido_count'] = Pedido.objects.count()
        context['estoque_baixo'] = Produto.objects.filter(estoque__lt=5).count()
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
    template_name = 'paginasweb/form-pedido.html'
    fields = ['cliente',  'forma_pagamento']
    success_url = reverse_lazy('listar_pedido')
    login_url = 'Login'
    extra_context = {'titulo': 'Finalizar Pedido', 'botao': 'Finalizar'}

    # Validar o formulário
    def form_valid(self, form):

        # Pega todos os itens
        itens = Itens.objects.filter(pedido__isnull=True)

        # Verifica se tem o estoque dos itens adicionados
        msg_erro_estoque = ""
        for item in itens:
            if item.produto.estoque < item.quantidade:
                msg_erro_estoque += f'Produto {item.produto.nome} sem estoque suficiente.\n'

        if msg_erro_estoque:
            form.add_error(None, msg_erro_estoque)
            return self.form_invalid(form)

        # Se não tem itens adicionados, da erro no formulário
        if not itens.exists():
            form.add_error(None, 'Adicione itens ao pedido.')
            return self.form_invalid(form)

        # Registra o pedido no banco de dados
        url = super().form_valid(form)

        # Calcula o valor total do pedido
        valor_total = 0

        for item in itens:
            # associa a este pedido
            item.pedido = self.object
            # diminuir o estoque do item
            item.produto.estoque -= item.quantidade
            # atualiza o banco de dados
            item.save()

            # Atualiza o valor total
            valor_total += item.valor_item

        # atualiza no banco o valor total correto
        self.object.valor_total = valor_total
        self.object.save()

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['itens'] = Itens.objects.filter(pedido__isnull=True)
        return context

class ItensCreate(LoginRequiredMixin, CreateView):
    model = Itens
    template_name = 'paginasweb/form.html'
    fields = ['produto', 'quantidade', 'observacao']
    success_url = reverse_lazy('listar_itens')
    login_url = 'Login'
    extra_context = {'titulo': 'Adicionar Item ao Pedido', 'botao': 'Adicionar'}

    def form_valid(self, form):
        form.instance.valor_item = form.instance.produto.preco * form.instance.quantidade
        return super().form_valid(form)


class CaixaCreate(LoginRequiredMixin, CreateView):
    model = Caixa
    template_name = 'paginasweb/form.html'
    fields = ['valor_inicial']
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
    template_name = 'paginasweb/form-pedido.html'
    fields = [ 'status']
    success_url = reverse_lazy('listar_pedido')
    login_url = 'Login'
    extra_context = {'titulo': 'Atualizar status do Pedido', 'botao': 'Atualizar', 'pedido': True}

class ItensUpdate(LoginRequiredMixin,  UpdateView):
    model = Itens
    template_name = 'paginasweb/form.html'
    fields = ['produto', 'quantidade', 'observacao']
    success_url = reverse_lazy('listar_itens')
    login_url = 'Login'
    extra_context = {'titulo': 'Editar Item do Pedido', 'botao': 'Atualizar'}

class CaixaUpdate(LoginRequiredMixin,   UpdateView):
    model = Caixa
    template_name = 'paginasweb/form.html'
    fields = [ 'valor_final']
    success_url = reverse_lazy('listar_caixa')
    login_url = 'Login'
    extra_context = {'titulo': 'Fechar Caixa', 'botao': 'Fechar'}

    def form_valid(self, form):
        form.instance.data_fechamento = timezone.now()
        return super().form_valid(form)

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
    extra_context = {'titulo': 'Lista de Produtos'}


class EstoqueBaixoList(ProdutoList):
    extra_context = {'titulo': 'Produtos com Estoque Baixo (menor que 5 unidades)'}
    def get_queryset(self):
        return super().get_queryset().filter(estoque__lt=5)
    

class PedidoList( ListView):
    model = Pedido
    template_name = 'paginasweb/listar_pedido.html'
    success_url = reverse_lazy('index')

class ItensList( ListView):
    model = Itens
    template_name = 'paginasweb/listar_itens.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return super().get_queryset().filter(pedido__isnull=True)

class CaixaList( ListView):
    model = Caixa
    template_name = 'paginasweb/listar_caixa.html'
    success_url = reverse_lazy('index')

class FormaPagamentoList( ListView):
    model = FormaPagamento
    template_name = 'paginasweb/listar_forma_pagamento.html'
    success_url = reverse_lazy('index')

