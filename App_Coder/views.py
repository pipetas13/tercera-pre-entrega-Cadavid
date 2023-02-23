from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#superuser : pipetas password: pipetas

# Create your views here.
from App_Coder.models import *
from App_Coder.forms import *

def inicio (request):
    return render(request, 'App_Coder/inicio.html')

def about (request):
    return render(request, 'App_Coder/about.html')

#Autentications Views
def registro(request):

    if request.method == "POST":

        miFormulario = RegistroFormulario(request.POST) #obtener los datos que están en el formulario
    
        if miFormulario.is_valid():

            miFormulario.save()

            return render(request, "App_Coder/inicio.html")

    else:

        miFormulario = RegistroFormulario()
    
    return render(request, "App_Coder/autentication/registro.html", {"formulario1":miFormulario})

def iniciar_sesion(request):

    if request.method == "POST":

        miFormulario = AuthenticationForm(request, data = request.POST) #obtener los datos que están en el formulario
    
        if miFormulario.is_valid():
            

            usuario = miFormulario.cleaned_data.get("username") #obteniendo el usuario y la contra ingresados
            contra = miFormulario.cleaned_data.get("password")

            miUsuario = authenticate(username=usuario, password=contra) #autentica que los datos de inicio sean correctos

            if miUsuario:

                login(request, miUsuario)
                mensaje = f"{miUsuario}"

                return render(request, "App_Coder/inicio.html", {"mensaje":mensaje})

        else:

            mensaje = f"Error. Ingresaste mal los datos."

            return render(request, "App_Coder/inicio.html", {"mensaje":mensaje})

    else:

        miFormulario = AuthenticationForm()
    
    return render(request, "App_Coder/autentication/login.html", {"formulario1":miFormulario})

#Solo usuarios con permisos de staff pueden crear artistas.
@login_required
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

#Solo los artistas pueden crear proyectos.
@login_required
def proyecto_formulario(request):
    if request.method =='POST':
        formulario3 = formulario_proyecto(request.POST)
        print(formulario3)
        if formulario3.is_valid():
            informacion = formulario3.cleaned_data
            Proyecto1 = proyectos(nombre = informacion['nombre'], cantidad = informacion['cantidad'], imagen = informacion['imagen']  )
            Proyecto1.save()
            return render (request, 'App_Coder/inicio.html')
    
    else:
        formulario3 = formulario_proyecto()
    return render (request, 'App_Coder/proyectos.html', {'formulario3':formulario3}) 

#CRUD de Projectos con vistas basadas en clases
class ProyectoLista(ListView): #por defecto el template name se llama curso_list.html
    model = proyectos
    template_name = "AppCoder/Proyectos/proyectos_list.html"
    
class ProyectoCrear(LoginRequiredMixin, CreateView): #por defecto el template name se llama curso_form.html
    model = proyectos
    fields = ["nombre", "cantidad","imagen"]
    success_url = "/AppCoder/Proyectos/lista"
    template_name = "AppCoder/Proyectos/proyectos_form.html"

class ProyectoBorrar(LoginRequiredMixin, DeleteView): #por defecto el template name se llama curso_confirm_delete.html
    model = proyectos
    success_url = "/AppCoder/Proyectos/lista"
    template_name = "AppCoder/Proyectos/proyectos_borrar.html"

class ProyectoEditar(LoginRequiredMixin, UpdateView): #usa el mismo html que el CreateView (curso_form.html)
    model = proyectos
    fields = ["nombre", "cantidad","imagen"]
    success_url = "/AppCoder/Proyectos/lista"
    template_name = "AppCoder/Proyectos/proyectos_form.html"

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

#Vista proyectos
def leerProyectos(request):

      proyecto = proyectos.objects.all() #trae todos los proyectos

      contexto= {"proyecto":proyecto} 

      return render(request, "AppCoder/proyectos.html",contexto)
