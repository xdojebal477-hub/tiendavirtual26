from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns=[
    path('tienda/admin/productos/listado',ListadoProductos.as_view(),name='listado'),
]