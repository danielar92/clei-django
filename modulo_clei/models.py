from django.db import models
# from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from personas.models import Persona, Autor



class Topico(models.Model):
    nombre = models.CharField(max_length=60)

class CLEI(models.Model):
    fechaInscripcionDescuento = models.DateTimeField()
    fechaInscripcion = models.DateTimeField()
    fechaTopeArticulo = models.DateTimeField()
    fechaNotificacion = models.DateTimeField()
    tarifaReducida = models.DateTimeField()
    tarifaNormal = models.DateTimeField()
    fechaInicio =  models.DateTimeField()
    topicos = models.ManyToManyField(Topico)
    cp = models.ForeignKey(Group)

    # cp = models.ForeignKey('personas.CP',related_name='cp_del_clei')
    #articulos =  models.ForeignKey(Articulo)
    # dias = 5

class Inscripcion(models.Model):
    dirPostal = models.CharField(max_length=60)
    pagWeb = models.URLField(max_length=60)
    telf = models.IntegerField()
    tipo = models.IntegerField()
    fecha = models.DateTimeField()
    clei = models.ForeignKey(CLEI)
    persona = models.ForeignKey(Persona)


class Articulo(models.Model):
    # ACEPTADO, RECHAZADO, REVISANDO, ESPERANDO = range(4)
    titulo = models.CharField(max_length=60)
    pclaves = models.CharField(max_length=60) # TIENEN QUE SER 5 CAMPOS
    # status = ESPERANDO
    status = models.IntegerField()
    note = models.IntegerField()
    # nota = 0
    correcciones = 0
    autores = models.ManyToManyField(Autor)
    topicos = models.ManyToManyField(Topico)
    # evaluadores = models.ManyToManyField()
    clei = models.ForeignKey(CLEI)

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
    lugar = models.ForeignKey(Lugar)
    tipo = models.CharField(max_length=60)

# class Ponencia(models.Model):
#     articulos = models.ManyToManyField(Articulo)
#     moderador = models.ForeignKey('personas.Persona',related_name='modera_ponencia')
#     ponente = models.ForeignKey('personas.Persona')

# class Charla(models.Model):
#     moderador = models.ForeignKey('personas.Persona',related_name='modera_charla')
#     charlista = models.ForeignKey('personas.Persona')

# # class Social(Evento):

# # class Apertura(Evento):

# # class Clausura(Evento):
