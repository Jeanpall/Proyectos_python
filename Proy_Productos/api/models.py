from datetime import date
from django.db import models
from decimal import Decimal
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Productos(models.Model):
    nomProducto = models.CharField(max_length=50)
    desProducto = models.CharField(max_length=200)
    catProducto = models.ForeignKey('Categorias', on_delete=models.CASCADE)
    canProducto = models.PositiveIntegerField(default=True)
    preProducto = models.PositiveBigIntegerField(default=True)
    estProducto = models.BooleanField(default=True)

    #Define la instancia en una cadena de texto
    def __str__(self):
        return self.nomProducto
    
# Clase el cual tiene categorias del producto    
class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
    codigo_categoria = models.CharField(max_length=50)
    fecha_creacion =  models.DateField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    #Define la instancia en una cadena de texto
    def __str__(self):
        return self.nombre
    
class OrdenItem(models.Model):
    Descuentos = (
        ('0', '0%'),
        ('5', '5%'),
        ('10', '10%'),
        ('15', '15%'),
        ('20', '20%'),
        ('25', '25%'),
        ('30', '30%'),
        ('35', '35%'),
        ('40', '40%'),
        ('45', '45%'),
        ('50', '50%'),
    )
    
    orden_id = models.ForeignKey('Orden', on_delete=models.CASCADE)
    producto_id = models.ForeignKey('Productos', on_delete=models.CASCADE, related_name='orden_items')
    cantidad = models.DecimalField(max_digits=5, decimal_places=2)
    precio = models.PositiveBigIntegerField(default=True)
    descuento = models.CharField(max_length=2, choices=Descuentos, default='0')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False, auto_created=True)

# Señal para calcular el total antes de guardar el OrdenItem
@receiver(pre_save, sender=OrdenItem)
def calcular_total_orden_item(sender, instance, **kwargs):
    precio_con_descuento = instance.precio * (1 - Decimal(instance.descuento) / 100)
    total = instance.cantidad * precio_con_descuento
    instance.total = total

# Clase Orden
class Orden(models.Model):
    numero_orden = models.CharField(max_length=255)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_factura = models.DateField(default=date.today)
    operador_id = models.ForeignKey('Operador', on_delete=models.CASCADE)
    cliente_id = models.ForeignKey('Cliente', on_delete=models.CASCADE)

    #Define la instancia en una cadena de texto
    def __str__(self):
        return self.numero_orden

#Clase Operador
class Operador(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    rol = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)

    #Define la instancia en una cadena de texto
    def __str__(self):
        return self.nombre
    
#Clase Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    fecha_creacion = models.DateField(auto_now_add=True)

    #Define la instancia en una cadena de texto
    def __str__(self):
        return self.nombre