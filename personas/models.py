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
    # articulos = models.ForeignKey('modulo_clei.Articulo')


# class Dict(models.Model):
#     articulo = models.ForeignKey('modulo_clei.Articulo')
#     nota = models.IntegerField()

# class MiembroCP(Persona):
#     esPresidente = models.BooleanField()
#     experticies = models.ManyToManyField('modulo_clei.Topico')
    # correcciones = models.ForeignKey(Dict,db_index=True)


# class CP(models.Model):
#     clei = models.ForeignKey('modulo_clei.CLEI',related_name='clei_asociado')
#     miembros = models.ManyToManyField(MiembroCP,related_name='miembros_cp')
#     presidente = models.ForeignKey(MiembroCP)
