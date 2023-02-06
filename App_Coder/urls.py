from django.urls import path 

from App_Coder.views import *

urlpatterns = [
    path('inicio/',inicio),
    path('agregar_profesor/',agregar_profesor),
]