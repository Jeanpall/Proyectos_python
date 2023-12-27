from rest_framework import serializers
from .models import Productos,Categorias, OrdenItem, Orden, Operador, Cliente

#Definicion de variass clases el cual trae todos los datos
class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        #fields = ['nomProducto', 'desProducto', 'canProducto']
        fields = '__all__'

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        #fields = ['nomProducto', 'desProducto', 'canProducto']
        fields = '__all__'

class OrdenItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenItem
        #fields = ['nomProducto', 'desProducto', 'canProducto']
        fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        #fields = ['nomProducto', 'desProducto', 'canProducto']
        fields = '__all__'

class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        #fields = ['nomProducto', 'desProducto', 'canProducto']
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        #fields = ['nomProducto', 'desProducto', 'canProducto']
        fields = '__all__'