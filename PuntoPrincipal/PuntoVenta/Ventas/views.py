from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import addClienteForm, EditarClienteForm
from .forms import ProductoForm
from .models import Producto

def Cliente_view(request):
    clientes = Cliente.objects.all()  # Obtén la lista de clientes
    form = addClienteForm()
    return render(request, 'cliente.html', {'form': form, 'clientes': clientes})


def add_Cliente_view(request):
    if request.method == 'POST':
        form = addClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cliente')
    else:
        form = addClienteForm()
    return render(request, 'add_cliente.html', {'form': form})




def edit_Cliente_view(request, cliente_id):
    cliente = get_object_or_404(Cliente, cliente_id=cliente_id)
    if request.method == 'POST':
        form = EditarClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('Cliente')
    else:
        form = EditarClienteForm(instance=cliente)
    return render(request, 'Ventas/editar_cliente.html', {'form': form, 'cliente_id': cliente_id})



def delete_Cliente_view(request, cliente_id):
    cliente = get_object_or_404(Cliente, cliente_id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('Cliente')
    return render(request, 'eliminar_cliente.html', {'cliente': cliente})

def ventas_view(request):
    return render(request, 'ventas.html')


def agregar_producto_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Inventario')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def lista_productos_view(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'lista_productos.html', {'productos': productos})

def edit_producto_view(request, producto_id):
    producto = get_object_or_404(Producto, producto_id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('Inventario')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

def eliminar_producto_view(request, producto_id):
    producto = get_object_or_404(Producto, producto_id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('Inventario')
    return render(request, 'eliminar_producto.html', {'producto': producto})


def inventario_view(request):
    productos = Producto.objects.all()
    form = ProductoForm()
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Inventario')

    return render(request, 'inventario.html', {'productos': productos, 'form': form})

def historial_ventas_view(request):
    # Lógica para manejar la vista del historial de ventas
    return render(request, 'historial_ventas.html')

def reportes_ventas_view(request):
    # Lógica para manejar la vista de los reportes de ventas
    return render(request, 'reportes_ventas.html')

def devoluciones_view(request):
    # Lógica para manejar la vista de devoluciones
    return render(request, 'devoluciones.html')

def facturas_view(request):
    # Lógica para manejar la vista de facturas
    return render(request, 'facturas.html')