#encoding:utf-8
from django.forms import ModelForm
from django import forms
from articulo.models import Articulo

class ArticuloForm(ModelForm):
	class Meta:
		model = Articulo