from django.shortcuts import render

#superuser : pipetas password: pipetas

from django.http import HttpResponse
# Create your views here.
from App_Coder.models import *
from App_Coder.forms import *


def inicio (request):
    return render(request, 'App_Coder/  inicio.html')

def cliente(request):
    return render(request, 'App_Coder/cliente.html')

def artista(request):
    return render(request, 'App_Coder/artistas.html')

def proyecto(request):
    return render(request, 'App_Coder/proyectos.html')

def cliente_formulario(request):
    if request.method =='POST':
        formulario1 = formulario_cliente(request.POST)
        print(formulario1)
        if formulario1.is_valid():
            informacion = formulario1.cleaned_data
            Cliente1 = cliente(nombre = informacion['nombre'], apellido = informacion['apellido'] , email=informacion['email'], edad = informacion['edad'])
            Cliente1.save()
            return render (request, 'App_Coder/inicio.html')
    
    else:
        formulario1 = formulario_cliente()
    return render (request, 'App_Coder/clienteformulario.html', {'formulario1':formulario1}) 