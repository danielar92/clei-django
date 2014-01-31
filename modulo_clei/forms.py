from django import forms
from modulo_clei.models import CLEI, Topico, Evaluacion

class CLEIForm(forms.ModelForm):
    class Meta:
        model = CLEI

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico

class EvaluarForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
    	exclude = ('evaluador',)