from django import forms
from django_countries.data import COUNTRIES
from registration.forms import RegistrationForm
from modulo_clei.models import Topico

class PersonaForm(RegistrationForm):
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    institucion = forms.CharField(max_length=60)
    pais = forms.ChoiceField(sorted([(k, v) for k,v in COUNTRIES.items()]))
    experticies = forms.ModelMultipleChoiceField(queryset=Topico.objects.all())
