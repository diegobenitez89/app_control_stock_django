from django.urls import path
from .views import home, listado_producto, nuevo_producto, modificar_producto, eliminar_producto

urlpatterns = [
    path('', home, name='home'),
    path('listado-producto', listado_producto, name='listado_producto'),
    path('nuevo-producto', nuevo_producto, name='nuevo_producto'),
    path('modificar-producto/<id>/', modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', eliminar_producto, name='eliminar_producto'),



]
