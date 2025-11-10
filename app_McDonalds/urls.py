from django.urls import path
from . import views

urlpatterns = [
    # INICIO
    path('', views.inicio_mcdonalds, name='inicio_mcdonalds'),

    # CLIENTES
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('ver_clientes/', views.ver_clientes, name='ver_clientes'),
    path('actualizar_cliente/<int:id_cliente>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('realizar_actualizacion_cliente/<int:id_cliente>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('borrar_cliente/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),

    # PEDIDOS
    path('agregar_pedido/', views.agregar_pedido, name='agregar_pedido'),
    path('ver_pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('actualizar_pedido/<int:id_pedido>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('realizar_actualizacion_pedido/<int:id_pedido>/', views.realizar_actualizacion_pedido, name='realizar_actualizacion_pedido'),
    path('borrar_pedido/<int:id_pedido>/', views.borrar_pedido, name='borrar_pedido'),
]
