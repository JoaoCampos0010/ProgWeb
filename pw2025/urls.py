
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Inclui todas as urls criadas lá no app paginasweb
    path('', include('paginasweb.urls')),
]
