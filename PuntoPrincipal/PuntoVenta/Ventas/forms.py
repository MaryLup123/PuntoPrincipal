from django import forms
from .models import Cliente
from .models import Producto

class addClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('primer_nombre', 'segundo_nombre', 'tercer_nombre', 'primer_apellido', 'segundo_apellido', 'direccion', 'telefono', 'email')
        labels = {
            'primer_nombre': 'Primer nombre: ',
            'segundo_nombre': 'Segundo nombre: ',
            'tercer_nombre': 'Tercer nombre: ',
            'primer_apellido': 'Primer apellido: ',
            'segundo_apellido': 'Segundo apellido (opcional): ',
            'direccion': 'Dirección: ',
            'telefono': 'Teléfono: ',
            'email': 'Correo: '
        }
        widgets = {
            'primer_nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el primer nombre'}),
            'segundo_nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el segundo nombre (opcional)'}),
            'tercer_nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el tercer nombre (opcional)'}),
            'primer_apellido': forms.TextInput(attrs={'placeholder': 'Ingrese el primer apellido'}),
            'segundo_apellido': forms.TextInput(attrs={'placeholder': 'Ingrese el segundo apellido (opcional)'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ingrese la dirección'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese el teléfono'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ingrese el correo electrónico'}),
        }
class EditarClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('primer_nombre', 'segundo_nombre', 'tercer_nombre', 'primer_apellido', 'segundo_apellido', 'direccion', 'telefono', 'email')
        labels = {
            'primer_nombre': 'Primer nombre: ',
            'segundo_nombre': 'Segundo nombre: ',
            'tercer_nombre': 'Tercer nombre: ',
            'primer_apellido': 'Primer apellido: ',
            'segundo_apellido': 'Segundo apellido: ',
            'direccion': 'Dirección: ',
            'telefono': 'Teléfono: ',
            'email': 'Correo: '
        }
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen', 'categoria']
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'stock': 'Stock',
            'imagen': 'Imagen',
            'categoria': 'Categoría',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'categoria': forms.CheckboxSelectMultiple(),
        }