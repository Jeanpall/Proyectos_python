from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProductosSerializer, CategoriasSerializer, OrdenItemSerializer, OrdenSerializer, OperadorSerializer, ClienteSerializer
from .models import Productos, Categorias, OrdenItem, Orden, Operador, Cliente

# Create your views here.
#Define varias clases con uos Query como consulta y serializar los datos
class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class OrdenItemViewSet(viewsets.ModelViewSet):
    queryset = OrdenItem.objects.all()
    serializer_class = OrdenItemSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class OperadorViewSet(viewsets.ModelViewSet):
    queryset = Operador.objects.all()
    serializer_class = OperadorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer