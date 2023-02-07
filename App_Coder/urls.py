from django.urls import path 

from App_Coder.views import *

urlpatterns = [
    path('inicio/',inicio, name='Inicio'),
    path('cliente/',cliente, name='Clients'),
    path('artista/',artista_formulario, name='Artists'),
    path('proyecto/',proyecto_formulario, name='Projects'),
    path('clienteformulario/',cliente_formulario, name='ClientForm'),
    path('busquedaProyecto',busquedaProyecto,name='BusquedaProyecto'),
    path('resultados/', resultados,name='ResultadosBusqueda'),
]