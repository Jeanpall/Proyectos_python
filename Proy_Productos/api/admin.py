from django.contrib import admin
from .models import Productos, Categorias, OrdenItem, Orden, Operador, Cliente

# Register your models here.
admin.site.register(Productos)
admin.site.register(Categorias)
admin.site.register(OrdenItem)
admin.site.register(Orden)
admin.site.register(Operador)
admin.site.register(Cliente)