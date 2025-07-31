from django.urls import path
from .views import (
    IndexView, SobreView,
    CategoriaCreate, ProdutoCreate, PedidoCreate, ItensCreate, CaixaCreate, FormaPagamentoCreate
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # LOGIN / LOGOUT
    path("entrar/", auth_views.LoginView.as_view(
        template_name='paginasweb/form.html',
        extra_context={'titulo': 'Entrar', 'botao': 'Entrar'}
    ), name="Login"),

    path("sair/", auth_views.LogoutView.as_view(), name="logout"),

    # Páginas principais
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),

    # Cadastro
    path("cadastrar/categoria/", CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path("cadastrar/produto/", ProdutoCreate.as_view(), name="cadastrar-produto"),
    path("cadastrar/pedido/", PedidoCreate.as_view(), name="cadastrar-pedido"),
    path("cadastrar/itens/", ItensCreate.as_view(), name="cadastrar-itens"),
    path("cadastrar/caixa/", CaixaCreate.as_view(), name="cadastrar-caixa"),
    path("cadastrar/forma-pagamento/", FormaPagamentoCreate.as_view(), name="cadastrar-forma-pagamento"),
]
