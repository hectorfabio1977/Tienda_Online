from django.urls import path
from . import views

urlpatterns = [
    path("Crear/",views.Proveedoresview,name = 'Proveedor' ),
    path("Consultas/",views.Consultarviews, name = 'Consultar'),
]