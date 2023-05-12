from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from AppTerceraPreEntrega.models import Cliente, Vendedor, Producto, Venta

def busquedaVenta(request):

    return render(request, "")

def buscar(request):
    respuesta = f"La venta solicitada es:"

def buscar_vendedor(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        resultado = Vendedor.objects.filter(username__contains=busqueda)
        contexto = {
            "object_list": resultado,
        }
        http_response = render(
            request=request,
            template_name='lista_vendedor.html',
            context=contexto,
        )
        return http_response

##--------------------------------------------
##--------------Views Cliente##---------------
##--------------------------------------------
class ClientesListView(ListView):
    model = Cliente
    template_name = 'lista_clientes.html'
    
class ClienteCreateView(CreateView):
    model = Cliente
    fields = ('nombre', 'apellido', 'email', 'telefono', 'dni')
    success_url = reverse_lazy('lista_clientes')


class ClienteDetailView(DetailView):
    model = Cliente
    success_url = reverse_lazy('lista_clientes')


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ('nombre', 'apellido', 'email', 'telefono', 'dni')
    success_url = reverse_lazy('lista_clientes')


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('lista_clientes')

##--------------------------------------------
##--------------Views Vendedor##--------------
##--------------------------------------------

class VendedorListView(ListView):
    model = Vendedor
    template_name = 'lista_Vendedor.html'
    
class VendedorCreateView(CreateView):
    model = Vendedor
    fields = ('username', 'nombre', 'apellido', 'email', 'telefono', 'dni', 'fcha_nacimiento')
    success_url = reverse_lazy('lista_vendedor')


class VendedorDetailView(DetailView):
    model = Vendedor
    success_url = reverse_lazy('lista_vendedor')


class VendedorUpdateView(UpdateView):
    model = Vendedor
    fields = ('nombre', 'apellido', 'email', 'telefono', 'dni', 'fcha_nacimiento')
    success_url = reverse_lazy('lista_vendedor')


class VendedorDeleteView(DeleteView):
    model = Vendedor
    success_url = reverse_lazy('lista_vendedor')


##--------------------------------------------
##--------------Views Vendedor##--------------
##--------------------------------------------
class ProductoListView(ListView):
    model = Producto
    template_name = 'lista_producto.html'
    
class ProductoCreateView(CreateView):
    model = Producto
    fields = ('nombre', 'marca', 'precio', 'stock')
    success_url = reverse_lazy('lista_producto')


class ProductoDetailView(DetailView):
    model = Producto
    success_url = reverse_lazy('lista_producto')


class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ('nombre', 'marca', 'precio', 'stock')
    success_url = reverse_lazy('lista_producto')


class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('lista_producto')

##--------------------------------------------
##--------------Views Vendedor##--------------
##--------------------------------------------
class VentaListView(ListView):
    model = Venta
    template_name = 'lista_venta.html'
    
class VentaCreateView(CreateView):
    model = Venta
    fields = ('username', 'cliente', 'producto', 'cantidad', 'preciotot')
    success_url = reverse_lazy('lista_venta')


class VentaDetailView(DetailView):
    model = Venta
    success_url = reverse_lazy('lista_venta')

class VentaDeleteView(DeleteView):
    model = Venta
    success_url = reverse_lazy('lista_venta')