from django.db import models
import uuid
# Modelo Cliente
class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10, unique=True, editable=False)  # Editable=False evita que se pueda cambiar manualmente
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True)
    tercer_nombre = models.CharField(max_length=100, blank=True, null=True)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.codigo:  # Genera el código solo si no existe
            self.codigo = str(uuid.uuid4())[:8].upper()  # Genera un código único de 8 caracteres
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['primer_nombre']

# Modelo CategoriaProducto
class CategoriaProducto(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'categoría de producto'
        verbose_name_plural = 'categorías de productos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

# Modelo Producto
class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    categoria = models.ManyToManyField(CategoriaProducto, related_name='productos', blank=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

# Modelo Venta
class Venta(models.Model):
    venta_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'venta'
        verbose_name_plural = 'ventas'
        ordering = ['-fecha_venta']

    def __str__(self):
        return f"Venta {self.venta_id} - {self.cliente.nombre}"

# Modelo DetalleVenta
class DetalleVenta(models.Model):
    detalle_id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'detalle de venta'
        verbose_name_plural = 'detalles de ventas'
        ordering = ['venta', 'producto']

    def __str__(self):
        return f"Detalle {self.detalle_id} - Venta {self.venta.venta_id}"