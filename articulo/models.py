from django.db import models
from django.forms import ModelForm
from django import forms

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
	autores = models.ManyToManyField('personas.Autor')
	topicos = models.ManyToManyField('modulo_clei.Topico')
	
	@property
	def nota(self):
		return 0

	@property
	def evaluadores(self):
		return None
