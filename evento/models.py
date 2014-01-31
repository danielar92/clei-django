from django.db import models
from modulo_clei.models import CLEI, Topico
from articulo.models import Articulo
from personas.models import Persona
from django.forms import ModelForm
from django import forms


class Lugar(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.TextField(max_length=140)
    capacidad = models.PositiveIntegerField()

    def __unicode__(self):
        return self.nombre

class Evento(models.Model):
	nombre = models.CharField(max_length=80)
	lugar = models.ForeignKey(Lugar)
	fecha = models.DateField()
	horaIni = models.TimeField(null=True)
	horaFin = models.TimeField(null=True)

	def __unicode__(self):
		return self.nombre

class Taller(Evento):
	pass
	
class Charla(Evento):
	charlista = models.ForeignKey(Persona, related_name='charlista_charla', null=True)
	moderador = models.ForeignKey(Persona, related_name='moderador_charla', null=True)
	
class Ponencia(Evento):
    articulos = models.ManyToManyField(Articulo)
    ponente = models.ForeignKey(Persona, related_name='ponente_ponencia', null=True)
    trabajos = models.ManyToManyField(Articulo, related_name='trabajos_ponencia', null=True)
    moderador = models.ForeignKey(Persona, related_name='moderador_ponencia', null=True)

class Apertura(Evento):
	pass
	
class Clausura(Evento):
	pass
	
class EventoSocial(Evento):
	pass
