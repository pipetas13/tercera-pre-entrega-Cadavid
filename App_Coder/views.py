from django.shortcuts import render

#superuser : pipetas password: pipetas

from django.http import HttpResponse
# Create your views here.
from App_Coder.models import *
from App_Coder.forms import *

def inicio (request):
    return render(request, 'App_Coder/inicio.html')

#def cliente(request):
#    return render(request, 'App_Coder/cliente.html')

#def artista(request):
#    return render(request, 'App_Coder/artistas.html')

#def proyecto(request):
#    return render(request, 'App_Coder/proyectos.html')

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

def artista_formulario(request):
    if request.method =='POST':
        formulario2 = formulario_artista(request.POST)
        print(formulario2)
        if formulario2.is_valid():
            informacion = formulario2.cleaned_data
            Artista1 = artista(nombre = informacion['nombre'], apellido = informacion['apellido'] , email=informacion['email'], edad = informacion['edad'],estilo = informacion['estilo'])
            Artista1.save()
            return render (request, 'App_Coder/inicio.html')
    
    else:
        formulario2 = formulario_artista()
    return render (request, 'App_Coder/artistas.html', {'formulario2':formulario2}) 

def proyecto_formulario(request):
    if request.method =='POST':
        formulario3 = formulario_proyecto(request.POST)
        print(formulario3)
        if formulario3.is_valid():
            informacion = formulario3.cleaned_data
            Proyecto1 = proyectos(nombre = informacion['nombre'], cantidad = informacion['cantidad'] )
            Proyecto1.save()
            return render (request, 'App_Coder/inicio.html')
    
    else:
        formulario3 = formulario_proyecto()
    return render (request, 'App_Coder/proyectos.html', {'formulario3':formulario3}) 

#Se crea la vista de busqueda

def busquedaProyecto(request):
    return render(request , 'App_Coder/busquedaProyecto.html')

def resultados(request):
    if request.GET["cantidad"]:
    #respuesta= f'Estoy buscando el proyecto: {request.get["nombre"]}'
        cantidad = request.GET['cantidad']
        proyecto = proyectos.objects.filter(cantidad__icontains=cantidad)
        return render(request,"App_Coder/resultadosBusqueda.html", {'proyecto':proyecto, 'cantidad':cantidad})
    else:
        respuesta='No existe el proyecto'
    return HttpResponse(respuesta)