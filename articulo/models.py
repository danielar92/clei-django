from django.db import models
from modulo_clei.models import CLEI, Topico
from personas.models import Persona

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
		return self.titulo

	@property
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

