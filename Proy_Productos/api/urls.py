from django.urls import path, include
from rest_framework import routers
from api import views

#Registra las vistas y define las URL
router = routers.DefaultRouter()
router.register(r'Productos', views.ProductosViewSet)
router.register(r'Categorias', views.CategoriasViewSet)
router.register(r'Operador', views.OperadorViewSet)
router.register(r'Cliente', views.ClienteViewSet)
router.register(r'Orden_Item', views.OrdenItemViewSet)
router.register(r'Orden', views.OrdenViewSet)

urlpatterns = [
    path('', include(router.urls))
]
