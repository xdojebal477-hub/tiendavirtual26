from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns=[
    path('tienda/admin/productos/listado',ListadoProductos.as_view(),name='listado'),
    path('tienda/admin/productos/editar/<int:pk>/',EditarProducto.as_view(),name='producto_editar'),
    path('tienda/admin/productos/eliminar/<int:pk>/',EliminarProducto.as_view(),name='producto_eliminar'),
    path('tienda/admin/productos/nuevo/',NuevoProducto.as_view(),name='producto_nuevo'),
    
]