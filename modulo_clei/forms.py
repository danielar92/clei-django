from django import forms
from modulo_clei.models import CLEI, Topico, CP
from personas.models import Persona

class CLEIForm(forms.ModelForm):
    miembros = forms.ModelMultipleChoiceField(queryset=Persona.objects.all())
    class Meta:
        model = CLEI

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico

# class CPForm(forms.ModelForm):
#     class Meta:
#         model = CP
