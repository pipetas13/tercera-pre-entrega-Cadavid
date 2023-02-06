from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from App_Coder.models import profesor

def inicio (request):
    return HttpResponse('Hola')

def agregar_profesor(request):
    profe1 = profesor(nombre = 'Pepe', apellido = 'Perez', email = 'pepe@perez.la',profesion = 'Profe', edad = 20)
    profe1.save()
    return HttpResponse('Se añade un usuario a la BD')