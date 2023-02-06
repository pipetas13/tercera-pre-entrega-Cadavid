from django.db import models

# Create your models here.
#Se crea la clase de cliente para RNDM DCKS(Nombre de la empresa de creación de NFTs)
class cliente(models.Model):
    nombre = models.CharField(max_length=40) #Mensajes de texto pequeños
    apellido = models.CharField(max_length=40) #Mensajes de texto pequeños
    email = models.EmailField()
    edad = models.IntegerField(default = None)

#Se crea la clase artista para RNDM DCKS
class artista(models.Model):
    nombre = models.CharField(max_length=40) #Mensajes de texto pequeños
    apellido = models.CharField(max_length=40) #Mensajes de texto pequeños
    email = models.EmailField()
    edad = models.IntegerField(default = None)
    estilo = models.CharField(max_length=40)

class proyectos(models.Model):
    nombre = models.CharField(max_length=40) #Mensajes de texto pequeños
    #instagram = models.EmailField()
    cantidad = models.IntegerField(default = None)
