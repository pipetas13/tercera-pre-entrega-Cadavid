from django.urls import path 
from App_Coder.views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static  import static
from django.conf import settings
urlpatterns = [
    path('',inicio, name='Inicio'),
    #urls autenticacion de usuario
    path("registro/",registro, name="Sign Up"),
    path("login/",iniciar_sesion, name="Sign In"),
    path("logout/",LogoutView.as_view(template_name="App_Coder/autentication/logout.html"), name="Logout"),

    #urls clases 
    path('about/',about, name='About'),
    path('artista/',artista_formulario, name='Artists'),
    path('proyecto/',proyecto_formulario, name='Projects'),

    #urls busqueda
    path('busquedaProyecto/',busquedaProyecto,name='BusquedaProyecto'),
    path('resultadosBusqueda/', resultados,name='ResultadosBusqueda'),

    # cruds 
    #CRUD de Cursos
    path('proyecto/',proyectos, name='Proyectos'),
    path("Proyectos/lista", ProyectoLista.as_view(), name = "Ver Proyectos"),
    path("Proyectos/nuevo", ProyectoCrear.as_view(), name = "Crear Proyectos"),
    path("Proyectos/borrar/<int:pk>", ProyectoBorrar.as_view(), name="Borrar Proyectos"),
    path("Proyectos/editar/<int:pk>", ProyectoEditar.as_view(), name="Editar Proyectos"),
]

urlpatterns += static[settings.MEDIA_URL,document_root=settings.MEDIA_ROOT]