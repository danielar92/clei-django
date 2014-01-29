from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from django import forms

def log_in_processor(request):
    return {'login_form': AuthenticationForm()}

def home(request):
    return render(request,'home.html')


def MostrarClei(request):
    return render(request,'crearCLEI.html')

def CrearClei(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
    else:
        form = CLEI()
    return render(request,'crearCLEI.html',{'cleiform':form})
