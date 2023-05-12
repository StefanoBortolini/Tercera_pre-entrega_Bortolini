from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


from AppTerceraPreEntrega.forms import ClienteFormulario
from AppTerceraPreEntrega.models import Cliente, Vendedor, Producto, Venta

# # Create your views here.
# def listar_clientes(request):
#     contexto = {
#         "clientes": Cliente.objects.all(),
#     }
#     http_response = render(
#         request=request,
#         template_name='lista_clientes.html',
#         context=contexto,
#     )
#     return http_response



# def crear_cliente(request):
#     if request.method == "POST":
#         formulario = ClienteFormulario(request.POST)

#         if formulario.is_valid():
#             data = formulario.cleaned_data  # es un diccionario
#             nombre = data["nombre"]
#             apellido = data["apellido"]
#             email = data["email"]
#             telefono = data["telefono"]
#             dni = data["dni"]
#             cliente = Cliente(nombre=nombre, apellido=apellido, email=email, telefono=telefono, dni=dni)  # lo crean solo en RAM
#             cliente.save()  # Lo guardan en la Base de datos

#             # Redirecciono al usuario a la lista de cursos
#             url_exitosa = reverse('lista_clientes')  # estudios/cursos/
#             return redirect(url_exitosa)
#     else:  # GET
#         formulario = ClienteFormulario()
#     http_response = render(
#         request=request,
#         template_name='formulario_cliente.html',
#         context={'formulario': formulario}
#     )
#     return http_response

##--------------Views Cliente##--------------
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
