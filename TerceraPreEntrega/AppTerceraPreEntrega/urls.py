from django.contrib import admin
from django.urls import path

from AppTerceraPreEntrega.views import ClientesListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

urlpatterns = [
    path('cliente/', ClientesListView.as_view(), name='lista_clientes'),
    path('cliente/<int:pk>/', ClienteDetailView.as_view(), name="ver_cliente"),
    path('cliente_form/', ClienteCreateView.as_view(), name="crear_cliente"),
    path('editar-cliente/<int:pk>/', ClienteUpdateView.as_view(), name="editar_cliente"),
    path('eliminar-cliente/<int:pk>/', ClienteDeleteView.as_view(), name="eliminar_cliente"),
]