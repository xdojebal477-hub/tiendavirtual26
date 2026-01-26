from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import ProductoForm,CompraForm
from decimal import Decimal, InvalidOperation
# Create your views here.
class ListadoProductos(ListView):
    model=Producto
    template_name='tienda/productos_lista.html'
    context_object_name='productos'

class ProductoDetalle(DetailView):
    model=Producto
    template_name='tienda/producto_detalle.html'
    context_object_name='producto'
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



class TiendaProducto(ListView):
#muestra un listado de los productos y es posible buscar y filtrar por varios campos.
    model = Producto
    template_name = 'tienda/tienda_productos.html'
    context_object_name = 'productos'

    def get_queryset(self):
        queryset = super().get_queryset().select_related('marca')

        # filtros (el template usa "buscar"; aceptamos también "nombre" por compatibilidad)
        buscar = (self.request.GET.get('buscar') or self.request.GET.get('nombre') or '').strip()
        marca_id = (self.request.GET.get('marca') or '').strip()
        

        if buscar:
            queryset = queryset.filter(nombre__icontains=buscar)

        if marca_id:
            # evita filtros raros si viene algo no numérico
            if marca_id.isdigit():
                queryset = queryset.filter(marca_id=int(marca_id))

        return queryset.order_by('nombre')

    def get_context_data(self, **kwargs):#llenamos el select de marcas
        context = super().get_context_data(**kwargs)
        context['marcas'] = Marca.objects.all()
        return context
    



class CheckoutProducto(CreateView):
    model=Compra
    form_class=CompraForm
    template_name='tienda/checkout.html'
    success_url=reverse_lazy('tienda_productos')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['producto']=get_object_or_404(Producto,pk=self.kwargs['pk'])
        return context
    
    
    def form_valid(self, form):
        producto = get_object_or_404(Producto, pk=self.kwargs['pk'])
        unidades = form.cleaned_data['unidades']
        
        if producto.unidades < unidades:
            form.add_error('unidades', 'No hay suficientes unidades disponibles.')
            return self.form_invalid(form)
            
        compra = form.save(commit=False)
        compra.producto = producto
        compra.usuario = self.request.user
        compra.importe = producto.precio * unidades
        compra.iva = compra.importe * Decimal('0.21')
        
        producto.unidades -= unidades
        producto.save()
        
        compra.save()
        
        # Actualizar saldo del usuario
        usuario = self.request.user
        usuario.saldo -= compra.importe + compra.iva
        usuario.save()
        
        return super().form_valid(form)