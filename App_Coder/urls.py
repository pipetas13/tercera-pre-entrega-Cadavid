from django.urls import path 

from App_Coder.views import *

urlpatterns = [
    path('inicio/',inicio, name='Inicio'),
    path('cliente/',cliente, name='Clients'),
    path('artista/',artista, name='Artists'),
    path('proyecto/',proyecto, name='Projects'),
    path('clienteformulario/',cliente_formulario, name='ClientForm'),
]