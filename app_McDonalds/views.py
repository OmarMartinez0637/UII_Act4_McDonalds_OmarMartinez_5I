from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Pedido
from datetime import date

# ==================================================
# INICIO
# ==================================================
def inicio_mcdonalds(request):
    return render(request, 'inicio.html')


# ==================================================
# CRUD CLIENTES
# ==================================================
def agregar_cliente(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono'),
            direccion=request.POST.get('direccion'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento')
        )
        return redirect('ver_clientes')
    return render(request, 'cliente/agregar_cliente.html')


def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})


def actualizar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})


def realizar_actualizacion_cliente(request, id_cliente):
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.email = request.POST.get('email')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion = request.POST.get('direccion')
        cliente.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        cliente.save()
        return redirect('ver_clientes')
    return redirect('ver_clientes')


def borrar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})


# ==================================================
# CRUD PEDIDOS
# ==================================================
def agregar_pedido(request):
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        id_cliente = request.POST.get('id_cliente')
        cliente = Cliente.objects.get(id_cliente=id_cliente)
        Pedido.objects.create(
            id_cliente=cliente,
            id_empleado=request.POST.get('id_empleado'),
            fecha_pedido=request.POST.get('fecha_pedido'),
            total=request.POST.get('total'),
            estado=request.POST.get('estado'),
            direccion=request.POST.get('direccion'),
            forma_pago=request.POST.get('forma_pago')
        )
        return redirect('ver_pedidos')
    return render(request, 'pedido/agregar_pedido.html', {'clientes': clientes})


def ver_pedidos(request):
    pedidos = Pedido.objects.select_related('id_cliente').all().order_by('-id_pedido')
    return render(request, 'pedido/ver_pedido.html', {'pedidos': pedidos})


def actualizar_pedido(request, id_pedido):
    pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
    clientes = Cliente.objects.all()
    return render(request, 'pedido/actualizar_pedido.html', {'pedido': pedido, 'clientes': clientes})


def realizar_actualizacion_pedido(request, id_pedido):
    if request.method == 'POST':
        pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
        cliente = Cliente.objects.get(id_cliente=request.POST.get('id_cliente'))
        pedido.id_cliente = cliente
        pedido.id_empleado = request.POST.get('id_empleado')
        pedido.fecha_pedido = request.POST.get('fecha_pedido')
        pedido.total = request.POST.get('total')
        pedido.estado = request.POST.get('estado')
        pedido.direccion = request.POST.get('direccion')
        pedido.forma_pago = request.POST.get('forma_pago')
        pedido.save()
        return redirect('ver_pedidos')
    return redirect('ver_pedidos')


def borrar_pedido(request, id_pedido):
    pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedidos')
    return render(request, 'pedido/borrar_pedido.html', {'pedido': pedido})
