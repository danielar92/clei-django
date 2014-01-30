from django import forms
from modulo_clei.models import CLEI, Topico

class CLEIForm(forms.ModelForm):
    class Meta:
        model = CLEI

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
