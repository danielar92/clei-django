from django.db import models
from django import forms

class Topico(models.Model):
    nombre = models.CharField(max_length=60)

    def __unicode__(self):
        return self.nombre

class CLEI(models.Model):
    fechaInscripcion = models.DateTimeField()
    fechaInscripcionDescuento = models.DateTimeField()
    fechaTopeArticulo = models.DateTimeField()
    fechaNotificacion = models.DateTimeField()
    tarifaReducida = models.FloatField()
    tarifaNormal = models.FloatField()
    fechaInicio =  models.DateTimeField()
    topicos = models.ManyToManyField(Topico, related_name='cleis')

    def __unicode__(self):
        return "CLEI del %s" % (self.fechaInicio.strftime("%Y"))

class CP(models.Model):
    miembros = models.ManyToManyField('personas.MiembroCP')
    clei = models.OneToOneField(CLEI, related_name='cp')


class Inscripcion(models.Model):
    dirPostal = models.CharField(max_length=60)
    pagWeb = models.URLField(max_length=60)
    telf = models.IntegerField()
    tipo = models.IntegerField()
    fecha = models.DateTimeField()
    clei = models.ForeignKey(CLEI, related_name='inscripciones')
    persona = models.ForeignKey('personas.Persona', related_name='inscripciones')

class Evaluacion(models.Model):
    articulo = models.ForeignKey('articulo.Articulo', related_name='correcciones')
    evaluador = models.ForeignKey('personas.Persona', related_name='evaluaciones')
    nota = models.IntegerField()

    class Meta:
        unique_together = ("articulo", "evaluador")
