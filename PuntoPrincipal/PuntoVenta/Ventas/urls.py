from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('historial_ventas/', views.historial_ventas_view, name='historial_ventas'),
    path('reportes_ventas/', views.reportes_ventas_view, name='reportes_ventas'),
    path('devoluciones/', views.devoluciones_view, name='devoluciones'),
    path('facturas/', views.facturas_view, name='facturas'),
    
    path('', views.ventas_view, name='Ventas'),
    path('Cliente/', views.Cliente_view, name='Cliente'),
    path('add_Cliente/', views.add_Cliente_view, name='AddCliente'),
    path('edit_Cliente/<int:cliente_id>/', views.edit_Cliente_view, name='EditCliente'),
    path('delete_Cliente/<int:cliente_id>/', views.delete_Cliente_view, name='DeleteCliente'),
    path('inventario/', views.inventario_view, name='Inventario'),
    path('inventario/agregar/', views.agregar_producto_view, name='agregar_producto'),
    path('productos/editar/<int:producto_id>/', views.edit_producto_view, name='edit_producto'),  # Ruta para editar un producto
    path('productos/eliminar/<int:producto_id>/', views.eliminar_producto_view, name='eliminar_producto'),  # Ruta para eliminar un producto
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)