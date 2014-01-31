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


