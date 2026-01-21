from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import ProductoForm
# Create your views here.
class ListadoProductos(ListView):
    model=Producto
    template_name='tienda/productos_lista.html'
    context_object_name='productos'
    
class EditarProducto(UpdateView):
    model=Producto
    form_class=ProductoForm
    template_name='tienda/producto_form.html'
    success_url=reverse_lazy('listado')
    
class NuevoProducto(CreateView):
    model=Producto
    form_class=ProductoForm
    template_name='tienda/producto_form.html'
    success_url=reverse_lazy('listado')
    
    
class EliminarProducto(DeleteView):
    model=Producto
    template_name='tienda/producto_eliminar.html'
    success_url=reverse_lazy('listado')