from django.contrib import admin
from django.urls import path

from AppTerceraPreEntrega.views import *

urlpatterns = [
    #Url Cliente
    path('cliente/', ClientesListView.as_view(), name='lista_clientes'),
    path('cliente/<int:pk>/', ClienteDetailView.as_view(), name="ver_cliente"),
    path('cliente_form/', ClienteCreateView.as_view(), name="crear_cliente"),
    path('editar-cliente/<int:pk>/', ClienteUpdateView.as_view(), name="editar_cliente"),
    path('eliminar-cliente/<int:pk>/', ClienteDeleteView.as_view(), name="eliminar_cliente"),
    #Url Vendedor
    path('vendedor/', VendedorListView.as_view(), name='lista_vendedor'),
    path('vendedor/<int:pk>/', VendedorDetailView.as_view(), name="ver_vendedor"),
    path('vendedor_form/', VendedorCreateView.as_view(), name="crear_vendedor"),
    path('editar-vendedor/<int:pk>/', VendedorUpdateView.as_view(), name="editar_vendedor"),
    path('eliminar-vendedor/<int:pk>/', VendedorDeleteView.as_view(), name="eliminar_vendedor"),
    #Url Producto
    path('producto/', ProductoListView.as_view(), name='lista_producto'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name="ver_producto"),
    path('producto_form/', ProductoCreateView.as_view(), name="crear_producto"),
    path('editar-producto/<int:pk>/', ProductoUpdateView.as_view(), name="editar_producto"),
    path('eliminar-producto/<int:pk>/', ProductoDeleteView.as_view(), name="eliminar_producto"),
]