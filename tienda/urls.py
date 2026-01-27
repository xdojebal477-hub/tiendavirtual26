from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns=[

    path('tienda/',TiendaProducto.as_view(),name='tienda_productos'),
    path('tienda/checkout/<int:pk>/',CheckoutProducto.as_view(),name='checkout'),

    path('tienda/admin/productos/listado',ListadoProductos.as_view(),name='listado'),
    
    
    path('tienda/admin/productos/detalle/<int:pk>/',ProductoDetalle.as_view(),name='producto_detalle'),
    path('tienda/admin/productos/editar/<int:pk>/',EditarProducto.as_view(),name='producto_editar'),
    path('tienda/admin/productos/eliminar/<int:pk>/',EliminarProducto.as_view(),name='producto_eliminar'),
    path('tienda/admin/productos/nuevo/',NuevoProducto.as_view(),name='producto_nuevo'),
    


    path('perfil/',PerfilDetalle.as_view(),name='perfil_detalle'),
    path('tienda/informes/',InformeVentas.as_view(),name='informe_ventas'),
]