from msilib.schema import ListView
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime

from .models import Articulo, Proveedor, Categoria

from .forms import FormularioProductos, FormularioArticuloDescuento, FormularioProveedor, FormularioCategoria

from django.contrib import messages

# Create your views here.

def home_view(request):
    template= 'stock/home.html'
    return render(request, template)

def listar_stock(request):
    template= 'stock/listar_stock.html'

    lista_articulos = Articulo.objects.all().order_by('-fecha')

    context = { 
        "lista_articulos": lista_articulos
    }
    return render(request, template, context)

# def detalle_articulo(request, pk):
#     template = 'stock/detalle_articulo.html'

#     articulo = Articulo.objects.get(id=pk)
    
#     context = { 
#         "articulo": articulo
#     }

#     return render(request, template, context)

def eliminar_articulo(request, pk):
    Articulo.objects.get(id=pk).delete()

    return HttpResponseRedirect(reverse('listar_stock'))

# def crear_articulo(request):
#     template = 'stock/crear_articulo.html'
#     context = {}

#     if request.method == 'GET':
#         context['form'] = FormularioArticuloDescuento()


#     if (request.method == 'POST'):
#         try:
#             producto = Articulo.objects.create(
#                 nada= request.POST['nombre'],
#                 precio= float(request.POST['precio']),
#                 descripcion = request.POST['descripcion'],
#                 fecha = datetime.now()
#                 )
#             messages.success(request, 'Producto creado satisfactoriamente.')
#             producto.save()
#             return HttpResponseRedirect(reverse('listar_stock'))
#         except:
#             messages.error(request, 'No se pudo crear el producto.')

#     return render(request, template, context)

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, DetailView


class CrearArticulo(CreateView):
    model = Articulo
    template_name = 'stock/crear_articulo.html'
    form_class = FormularioArticuloDescuento
    #fields = ['nombre', 'precio', 'fecha', 'descripcion', 'imagenprod', 'categoria']
    success_url = reverse_lazy('listar_stock')

    def form_valid(self, form):
        f = form.save(commit=False)
        f.fecha = datetime.now()
        f = form.save(commit=True)

        return super(CrearArticulo, self).form_valid(form)



class ListarArticulos(ListView):
    model = Articulo
    paginate_by = 3
    template_name = 'stock/listar_stock.html'
    context_object_name = 'lista_articulos'

class BusquedaArticulos(ListView):
    model = Articulo
    paginate_by = 3
    template_name = 'stock/busqueda_stock.html'
    context_object_name = 'lista_articulos'

    def get_queryset(self):
        queryset = Articulo.objects.all()
  
        nombre_articulo = self.request.GET.get('nombre')

        if nombre_articulo is not None:
            queryset = queryset.filter(nombre__icontains=nombre_articulo)
        
        return queryset

class ActualizarArticulo(UpdateView):
    model = Articulo
    template_name = 'stock/editar_articulo.html'
    form_class = FormularioArticuloDescuento
    #fields = ['nombre', 'precio', 'descripcion']
    success_url = reverse_lazy('listar_stock')

class EliminarArticulo(DeleteView):
    model = Articulo
    template_name = 'stock/eliminar_articulo.html'
    success_url = reverse_lazy('listar_stock')

class DetalleArticulo(DetailView):
    model = Articulo
    template_name = 'stock/detalle_articulo.html'


# Views de Proveedores
class ListarProveedores(ListView):
    model = Proveedor
    paginate_by = 3
    template_name = 'proveedores/listar.html'
    context_object_name = 'lista_proveedores'

class CrearProveedor(CreateView):
    model = Proveedor
    template_name = 'proveedores/crear_proveedor.html'
    form_class = FormularioProveedor
    success_url = reverse_lazy('listar_proveedores')

class ActualizarProveedores(UpdateView):
    model = Proveedor
    template_name =  'proveedores/actualizar_proveedor.html'
    form_class = FormularioProveedor
    success_url = reverse_lazy('listar_proveedores')

class EliminarProveedores(DeleteView):
    model = Proveedor
    template_name = 'proveedores/eliminar_proveedor.html'
    success_url = reverse_lazy('listar_proveedores')

# Views de Categorias
class ListarCategorias(ListView):
    model = Categoria
    paginate_by = 3
    template_name = 'categorias/listar.html'
    context_object_name = 'lista_categoria'

class CrearCategorias(CreateView):
    model = Categoria
    template_name = 'categorias/crear_categoria.html'
    form_class = FormularioCategoria
    success_url = reverse_lazy('listar_categorias')

class ActualizarCategorias(UpdateView):
    model = Categoria
    template_name =  'categorias/actualizar_categoria.html'
    form_class = FormularioCategoria
    success_url = reverse_lazy('listar_categorias')

class EliminarCategorias(DeleteView):
    model = Categoria
    template_name = 'categorias/eliminar_categoria.html'
    success_url = reverse_lazy('listar_categorias')
