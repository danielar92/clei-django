from django.db import models
from django import forms
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Persona(User):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    institucion  = models.CharField(max_length=60)
    pais = CountryField()
    dirPostal = models.CharField(max_length=60)
    pagWeb = models.URLField(max_length=60)
    telf = models.IntegerField()
    experticies = models.ManyToManyField('modulo_clei.Topico')

    def __unicode__(self):
        return "%s %s" % (self.nombre, self.apellido)

# class Autor(Persona):


# class MiembroCP(Persona):
