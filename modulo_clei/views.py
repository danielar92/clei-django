from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from django import forms
from modulo_clei.models import CLEI
from django.db import models
from django.forms import ModelForm


class CLEIForm(ModelForm):
    class Meta:
        model = CLEI
        fields = ['fechaInscripcionDescuento','fechaInscripcion','fechaTopeArticulo','fechaNotificacion','tarifaReducida','tarifaNormal','fechaInicio']

def log_in_processor(request):
    return {'login_form': AuthenticationForm()}

def home(request):
    return render(request,'home.html')


def MostrarClei(request):
    return render(request,'crearCLEI.html')

def CrearClei(request):
    if request.method == 'POST':
        form = CLEIForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CLEIForm()
    return render(request,'crearCLEI.html',{'cleiform':form})
