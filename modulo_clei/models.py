from django.utils import timezone
from django.db import models
from personas.models import Persona



class Topico(models.Model):
    nombre = models.CharField(max_length=60)

    def __unicode__(self):
        return self.nombre

class CLEI(models.Model):
    fechaInscripcionDescuento = models.DateTimeField('Fecha de inscripcion con descuento', help_text='hasta esta fecha se haran las incripciones con descuento')
    fechaInscripcion = models.DateTimeField('Fecha de inscripcion', help_text='fecha maxima de inscripcion')
    fechaTopeArticulo = models.DateTimeField('Fecha tope de envio de articulos', help_text='Fecha hasta la que se reciben articulos')
    fechaNotificacion = models.DateTimeField('Fecha notificacion', help_text='Fecha en la que se envian los emails de notificacion')
    tarifaReducida = models.FloatField('Tarifa Reducida')
    tarifaNormal = models.FloatField('Tarifa Normal')
    fechaInicio =  models.DateTimeField('Fecha de Inicio CLEI')
    topicos = models.ManyToManyField(Topico, related_name='cleis')

    @property
    def puede_enviar(self):
        return self.fechaTopeArticulo > timezone.now()

    @property
    def puede_inscribir(self):
        return self.fechaInscripcion > timezone.now()

    @property
    def costo_inscripcion(self):
        if timezone.now() < self.fechaInscripcionDescuento:
            return self.tarifaReducida

        return self.tarifaNormal

    def inscrito(self, user):
        return user.persona.inscripciones.filter(clei=self).exists()

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('clei_detail', args=[self.pk])

    def __unicode__(self):
        return "CLEI del %s" % (self.fechaInicio.strftime("%Y"))

class CP(models.Model):
    miembros = models.ManyToManyField(Persona)
    clei = models.OneToOneField(CLEI, related_name='cp')

    def __unicode__(self):
        return "CP del %s" % self.clei


class Inscripcion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    clei = models.ForeignKey(CLEI, related_name='inscripciones')
    persona = models.ForeignKey(Persona, related_name='inscripciones')
    costo = models.FloatField()

    def __unicode__(self):
        return "Inscripcion de %s en el %s" % (self.persona, self.clei)

    class Meta:
        unique_together = ("clei", "persona")


ACEPTADO, RECHAZADO, REVISANDO, ESPERANDO = range(4)
STATUS_CHOICES = (
    (ACEPTADO, "Aceptado"),
    (RECHAZADO, "Rechazado"),
    (REVISANDO, "En Revision"),
    (ESPERANDO, "En Espera"),
)
class Articulo(models.Model):
    titulo = models.CharField(max_length=60)
    pclaves = models.TextField("Palabras claves", help_text="hasta 5 palabras claves, separadas por coma", max_length=60,)
    status = models.IntegerField(choices=STATUS_CHOICES, default=ESPERANDO)
    autores = models.ManyToManyField(Persona, related_name='articulos')
    topicos = models.ManyToManyField(Topico)
    clei = models.ForeignKey(CLEI, related_name='articulos', null=True, blank=True)

    def __unicode__(self):
        return self.titulo

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
