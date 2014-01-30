#encoding:utf-8
from django.forms import ModelForm
from django import forms
from evento.models import Lugar, Evento, Charla, Ponencia

class LugarForm(ModelForm):
	class Meta:
		model = Lugar

class CharlaForm(ModelForm):
	class Meta:
		model = Charla
		exclude = ('tipo',)
		
		
	def clean_horaFin(self):
		ini = self.cleaned_data['horaIni']
		fin = self.cleaned_data['horaFin']
		if (fin <= ini):
			raise forms.ValidationError("Como termina antes de que empieza?!")
			
		return fin
		
class PonenciaForm(ModelForm):		
	class Meta:
		model = Ponencia
		exclude = ('tipo',)

	def clean_horaFin(self):
		ini = self.cleaned_data['horaIni']
		fin = self.cleaned_data['horaFin']
		if (fin <= ini):
			raise forms.ValidationError("Como termina antes de que empieza?!")
			
		return fin
		
class TallerForm(ModelForm):
	class Meta:
		model = Taller
		exclude = ('tipo',)

	def clean_horaFin(self):
		ini = self.cleaned_data['horaIni']
		fin = self.cleaned_data['horaFin']
		if (fin <= ini):
			raise forms.ValidationError("Como termina antes de que empieza?!")
			
		return fin

		
class AperturaForm(ModelForm):
	class Meta:
		model = Apertura
		exclude = ('tipo',)

	def clean_horaFin(self):
		ini = self.cleaned_data['horaIni']
		fin = self.cleaned_data['horaFin']
		if (fin <= ini):
			raise forms.ValidationError("Como termina antes de que empieza?!")
			
		return fin
		
class ClausuraForm(ModelForm):
	class Meta:
		model = Clausura
		exclude = ('tipo',)

	def clean_horaFin(self):
		ini = self.cleaned_data['horaIni']
		fin = self.cleaned_data['horaFin']
		if (fin <= ini):
			raise forms.ValidationError("Como termina antes de que empieza?!")
			
		return fin
		
class EventoSocialForm(ModelForm):
	class Meta:
		model = EventoSocial
		exclude = ('tipo',)
		
	def clean_horaFin(self):
		ini = self.cleaned_data['horaIni']
		fin = self.cleaned_data['horaFin']
		if (fin <= ini):
			raise forms.ValidationError("Como termina antes de que empieza?!")
			
		return fin
		
