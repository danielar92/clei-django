from django import forms
from modulo_clei.models import CLEI, Topico, CP, Articulo
from personas.models import Persona

class CLEIForm(forms.ModelForm):
    miembros = forms.ModelMultipleChoiceField(queryset=Persona.objects.all())
    class Meta:
        model = CLEI

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        exclude = ['clei', 'status']

# class CPForm(forms.ModelForm):
#     class Meta:
#         model = CP
