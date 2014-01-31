#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Articulo
from personas.models import Persona

class ArticuloForm(forms.ModelForm):
    def clean_pclaves(self):
        data = self.cleaned_data['pclaves']
        if len(data.split(',')) > 5:
            raise forms.ValidationError("A lo sumo debes especificar 5 palabras claves!")
        return data

    class Meta:
        model = Articulo
        exclude = ['clei', 'status']

