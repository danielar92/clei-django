#encoding:utf-8
from django.db import models
from modulo_clei.models import CLEI, Topico, Articulo
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
	horaIni = models.TimeField()
	horaFin = models.TimeField()

	def __unicode__(self):
		return self.nombre

class Taller(Evento):
	pass
	
class Charla(Evento):
	charlista = models.ForeignKey(Persona, related_name='charlista_charla')
	moderador = models.ForeignKey(Persona, related_name='moderador_charla')
	
class Ponencia(Evento):
	ponente = models.ForeignKey(Persona, related_name='ponente_ponencia')
	trabajos = models.ManyToManyField(Articulo, related_name='trabajos_ponencia')
	moderador = models.ForeignKey(Persona, related_name='moderador_ponencia')

class Apertura(Evento):
	pass
	
class Clausura(Evento):
	pass
	
class EventoSocial(Evento):
	pass
