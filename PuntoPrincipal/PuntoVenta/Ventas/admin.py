from django.contrib import admin
from .models import Cliente, CategoriaProducto, Producto, Venta, DetalleVenta

# Register your models here.
# Personalización de la administración para el modelo Cliente
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'primer_nombre', 'segundo_nombre', 'tercer_nombre', 'primer_apellido', 'segundo_apellido', 'telefono', 'email')
    search_fields = ['primer_nombre', 'primer_apellido', 'codigo']
    readonly_fields = ('codigo',)  # Campo solo lectura (por ejemplo, si quieres que no se modifique)

# Personalización de la administración para el modelo CategoriaProducto
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')  # Mostrar estos campos en la lista
    search_fields = ['nombre']  # Campo por el cual se puede buscar

# Personalización de la administración para el modelo Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'get_categorias')  # Mostrar estos campos en la lista
    search_fields = ['nombre']  # Campo por el cual se puede buscar
    list_filter = ('categoria',)  # Filtros en la barra lateral
    readonly_fields = ('precio',)  # Campo solo lectura
    filter_horizontal = ('categoria',)  # Muestra el campo ManyToMany en horizontal

    def get_categorias(self, obj):
        return ", ".join([c.nombre for c in obj.categoria.all()])
    get_categorias.short_description = 'Categorías'

# Personalización de la administración para el modelo Venta
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_venta', 'total')  # Mostrar estos campos en la lista
    search_fields = ['cliente__nombre']  # Buscar por nombre del cliente
    list_filter = ('fecha_venta',)  # Filtro por fecha de venta
    readonly_fields = ('fecha_venta', 'total')  # Campos solo lectura

# Personalización de la administración para el modelo DetalleVenta
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'cantidad', 'precio_unitario', 'subtotal')  # Mostrar estos campos en la lista
    search_fields = ['venta__cliente__nombre', 'producto__nombre']  # Buscar por nombre del cliente o producto
    readonly_fields = ('subtotal',)  # Campo solo lectura

# Registro de los modelos en la administración con su configuración personalizada
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(DetalleVenta, DetalleVentaAdmin)