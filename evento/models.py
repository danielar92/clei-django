from django.db import models
from articulo.models import Articulo
from personas.models import Persona

class Lugar(models.Model):
    nombre = models.CharField(max_length=60)
    ubicacion = models.CharField(max_length=60)
    capacidad = models.IntegerField()
    #eventos = models.ManyToManyField(Evento)

class Evento(models.Model):
    nombre = models.CharField(max_length=60)
    fecha = models.DateTimeField()
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    lugar = models.ForeignKey(Lugar, related_name='eventos')
    # tipo = models.CharField(max_length=60)

class Ponencia(Evento):
    articulos = models.ManyToManyField(Articulo)
    moderador = models.ForeignKey(Persona, related_name='ponencias_moderadas')
    ponente = models.ForeignKey(Persona)

class Charla(Evento):
    moderador = models.ForeignKey('personas.Persona',related_name='charlas_moderadas')
    presentador = models.ForeignKey('personas.Persona')

class Social(Evento):
    pass

class Apertura(Evento):
    pass

class Clausura(Evento):
    pass


# Create your models here.
