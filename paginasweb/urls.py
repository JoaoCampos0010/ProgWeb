from django.urls import path
from .views import IndexView, SobreView
from django.urls import path
from .views import (
    IndexView, SobreView,
    CategoriaCreate, ProdutoCreate, PedidoCreate, ItensCreate, CaixaCreate, FormaPagamentoCreate,
    CategoriaUpdate, ProdutoUpdate, PedidoUpdate, ItensUpdate, CaixaUpdate, FormaPagamentoUpdate,
    CategoriaDelete, ProdutoDelete, PedidoDelete, ItensDelete, CaixaDelete, FormaPagamentoDelete
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("sobre/", SobreView.as_view(), name="sobre"),

    # CREATE
    path("cadastrar/categoria/", CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path("cadastrar/produto/", ProdutoCreate.as_view(), name="cadastrar-produto"),
    path("cadastrar/pedido/", PedidoCreate.as_view(), name="cadastrar-pedido"),
    path("cadastrar/itens/", ItensCreate.as_view(), name="cadastrar-itens"),
    path("cadastrar/caixa/", CaixaCreate.as_view(), name="cadastrar-caixa"),
    path("cadastrar/forma-pagamento/", FormaPagamentoCreate.as_view(), name="cadastrar-forma-pagamento"),

    # UPDATE
    path("editar/categoria/<int:pk>/", CategoriaUpdate.as_view(), name="editar-categoria"),
    path("editar/produto/<int:pk>/", ProdutoUpdate.as_view(), name="editar-produto"),
    path("editar/pedido/<int:pk>/", PedidoUpdate.as_view(), name="editar-pedido"),
    path("editar/itens/<int:pk>/", ItensUpdate.as_view(), name="editar-itens"),
    path("editar/caixa/<int:pk>/", CaixaUpdate.as_view(), name="editar-caixa"),
    path("editar/forma-pagamento/<int:pk>/", FormaPagamentoUpdate.as_view(), name="editar-forma-pagamento"),

    # DELETE
    path("excluir/categoria/<int:pk>/", CategoriaDelete.as_view(), name="excluir-categoria"),
    path("excluir/produto/<int:pk>/", ProdutoDelete.as_view(), name="excluir-produto"),
    path("excluir/pedido/<int:pk>/", PedidoDelete.as_view(), name="excluir-pedido"),
    path("excluir/itens/<int:pk>/", ItensDelete.as_view(), name="excluir-itens"),
    path("excluir/caixa/<int:pk>/", CaixaDelete.as_view(), name="excluir-caixa"),
    path("excluir/forma-pagamento/<int:pk>/", FormaPagamentoDelete.as_view(), name="excluir-forma-pagamento"),
]
