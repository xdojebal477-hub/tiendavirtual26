from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView,DeleteView

# Create your views here.
class ListadoProductos(ListView):
    model=Producto
    template_name='tienda/productos_lista.html'
    context_object_name='productos'