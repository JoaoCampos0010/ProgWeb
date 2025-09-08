from django.urls import path
from .views import (
    IndexView, SobreView,
    CategoriaCreate, ProdutoCreate, PedidoCreate, ItensCreate, CaixaCreate, FormaPagamentoCreate,
    CategoriaUpdate, ProdutoUpdate, PedidoUpdate, ItensUpdate, CaixaUpdate, FormaPagamentoUpdate,
    CategoriaDelete, ProdutoDelete, PedidoDelete, ItensDelete, CaixaDelete, FormaPagamentoDelete,
    CategoriaList, ProdutoList, PedidoList, ItensList, CaixaList, FormaPagamentoList, EstoqueBaixoList
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # LOGIN / LOGOUT
    path("entrar/", auth_views.LoginView.as_view(
        template_name='paginasweb/form.html',
        extra_context={'titulo': 'Entrar', 'botao': 'Entrar'}
    ), name="Login"),

    path("sair/", auth_views.LogoutView.as_view(next_page="Login"), name="logout"),

    # Páginas principais
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),

    # Cadastro
    path("cadastrar/categoria/", CategoriaCreate.as_view(), name="cadastrar_categoria"),
    path("cadastrar/produto/", ProdutoCreate.as_view(), name="cadastrar_produto"),
    path("finalizar/pedido/", PedidoCreate.as_view(), name="cadastrar_pedido"),
    path("cadastrar/itens/", ItensCreate.as_view(), name="cadastrar_itens"),
    path("cadastrar/caixa/", CaixaCreate.as_view(), name="cadastrar_caixa"),
    path("cadastrar/forma-pagamento/", FormaPagamentoCreate.as_view(), name="cadastrar_forma_pagamento"),

    # Atualização
    path("atualizar/categoria/<int:pk>/", CategoriaUpdate.as_view(), name="atualizar_categoria"),
    path("atualizar/produto/<int:pk>/", ProdutoUpdate.as_view(), name="atualizar_produto"),
    path("atualizar/pedido/<int:pk>/", PedidoUpdate.as_view(), name="atualizar_pedido"),
    path("atualizar/itens/<int:pk>/", ItensUpdate.as_view(), name="atualizar_itens"),
    path("atualizar/caixa/<int:pk>/", CaixaUpdate.as_view(), name="atualizar_caixa"),
    path("atualizar/forma-pagamento/<int:pk>/", FormaPagamentoUpdate.as_view(), name="atualizar_forma_pagamento"),

    # Exclusão
    path("excluir/categoria/<int:pk>/", CategoriaDelete.as_view(), name="excluir_categoria"),
    path("excluir/produto/<int:pk>/", ProdutoDelete.as_view(), name="excluir_produto"),
    path("excluir/pedido/<int:pk>/", PedidoDelete.as_view(), name="excluir_pedido"),
    path("excluir/itens/<int:pk>/", ItensDelete.as_view(), name="excluir_itens"),
    path("excluir/caixa/<int:pk>/", CaixaDelete.as_view(), name="excluir_caixa"),
    path("excluir/forma-pagamento/<int:pk>/", FormaPagamentoDelete.as_view(), name="excluir_forma_pagamento"),

    # Listagem
    path("listar/categoria/", CategoriaList.as_view(), name="listar_categoria"),
    path("listar/produto/", ProdutoList.as_view(), name="listar_produto"),
    path("listar/estoque-baixo/", EstoqueBaixoList.as_view(), name="listar_estoque_baixo"),
    path("listar/pedido/", PedidoList.as_view(), name="listar_pedido"),
    path("listar/itens/", ItensList.as_view(), name="listar_itens"),
    path("listar/caixa/", CaixaList.as_view(), name="listar_caixa"),
    path("listar/forma-pagamento/", FormaPagamentoList.as_view(), name="listar_forma_pagamento"),


]
