from django.db import models
from django import forms
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Persona(User):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    institucion  = models.CharField(max_length=60)

class Autor(Persona):
    pais = CountryField()

class MiembroCP(Persona):
    experticies = models.ManyToManyField('modulo_clei.Topico')
