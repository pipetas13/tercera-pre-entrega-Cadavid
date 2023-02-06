from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from App_Coder.models import *

def inicio (request):
    return render(request, 'App_Coder/inicio.html')

def cliente(request):
    cliente1 = cliente(nombre = 'Pepe', apellido = 'Perez', email = 'pepe@perez.la', edad = 20)
    cliente.save()
    return HttpResponse('Se añade un cliente a la BD')

def artista(request):
    artista1 = artista(nombre = 'Maria', apellido = 'Quevedo', email = 'maria@quevedo.rndmdcks', edad = 20, estilo= 'Caricatura')
    artista1.save()
    return HttpResponse('Se añade un artista a la BD')

def proyecto(request):
    proyecto1 = proyectos(nombre = 'E-Monsters', cantidad = 11111)
    proyecto1.save()
    return HttpResponse('Se añade un cliente a la BD')

