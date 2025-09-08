from django.contrib import admin
from .models import Categoria, FormaPagamento, Caixa, Produto, Pedido, Itens, Status

admin.site.register(Categoria)
admin.site.register(FormaPagamento)
admin.site.register(Caixa)
admin.site.register(Produto)
admin.site.register(Status)
admin.site.register(Pedido)
admin.site.register(Itens)
# Register your models here.
