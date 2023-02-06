from django.urls import path 

from App_Coder.views import *

urlpatterns = [
    path('inicio/',inicio),
    path('cliente/',cliente),
    path('artista/',artista),
    path('proyecto/',proyecto),
]