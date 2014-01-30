from django.db import models
from personas.models import Persona



class Topico(models.Model):
    nombre = models.CharField(max_length=60)

    def __unicode__(self):
        return self.nombre

class CLEI(models.Model):
    fechaInscripcionDescuento = models.DateTimeField()
    fechaInscripcion = models.DateTimeField()
    fechaTopeArticulo = models.DateTimeField()
    fechaNotificacion = models.DateTimeField()
    tarifaReducida = models.FloatField()
    tarifaNormal = models.FloatField()
    fechaInicio =  models.DateTimeField()
    topicos = models.ManyToManyField(Topico, related_name='cleis')

    def __unicode__(self):
        return "CLEI del %s" % (self.fechaInicio.strftime("%Y"))

class CP(models.Model):
    miembros = models.ManyToManyField(Persona)
    clei = models.OneToOneField(CLEI, related_name='cp')

    def __unicode__(self):
        return "CP del %s" % self.clei


class Inscripcion(models.Model):
    dirPostal = models.CharField(max_length=60)
    pagWeb = models.URLField(max_length=60)
    telf = models.IntegerField()
    tipo = models.IntegerField()
    fecha = models.DateTimeField()
    clei = models.ForeignKey(CLEI, related_name='inscripciones')
    persona = models.ForeignKey(Persona, related_name='inscripciones')


ACEPTADO, RECHAZADO, REVISANDO, ESPERANDO = range(4)
STATUS_CHOICES = (
    (ACEPTADO, "Aceptado"),
    (RECHAZADO, "Rechazado"),
    (REVISANDO, "En Revision"),
    (ESPERANDO, "En Espera"),
)
class Articulo(models.Model):
    titulo = models.CharField(max_length=60)
    pclaves = models.TextField(max_length=60)
    status = models.IntegerField(choices=STATUS_CHOICES, default=ESPERANDO)
    autores = models.ManyToManyField(Persona)
    topicos = models.ManyToManyField(Topico)
    clei = models.ForeignKey(CLEI, related_name='articulos')

    @property
    def nota(self):
        return 0

    @property
    def evaluadores(self):
        return None

class Evaluacion(models.Model):
    articulo = models.ForeignKey(Articulo, related_name='correcciones')
    evaluador = models.ForeignKey(Persona, related_name='evaluaciones')
    nota = models.IntegerField()

    class Meta:
        unique_together = ("articulo", "evaluador")

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
