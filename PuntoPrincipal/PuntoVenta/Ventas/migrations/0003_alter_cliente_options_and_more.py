# Generated by Django 5.1 on 2024-08-15 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['primer_nombre'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='nombre',
            new_name='primer_apellido',
        ),
        migrations.AddField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(default='TEMP0001', editable=False, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='primer_nombre',
            field=models.CharField(default='NombreTemporal', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='segundo_apellido',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='segundo_nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tercer_nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
