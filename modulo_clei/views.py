from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from django import forms
from modulo_clei.models import CLEI,Topico
from django.db import models
from django.forms import ModelForm

from django.views.generic import CreateView, ListView, UpdateView
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin


from .forms import CLEIForm, TopicoForm


def log_in_processor(request):
    return {'login_form': AuthenticationForm()}

def home(request):
    return render(request,'home.html')

class TopicoCreateView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = Topico
    form_class = TopicoForm
    template_name = 'crearTopico.html'
    success_url = '/clei/topicos/list'

class TopicoListView(LoginRequiredMixin, SuperuserRequiredMixin, ListView):
    model = Topico
    context_object_name = 'topicos'
    template_name = 'listarTopicos.html'

class TopicoUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    model = Topico
    template_name = 'actualizarTopico.html'
    success_url = '/clei/topicos/list'

class CLEICreateView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = CLEI
    form_class = CLEIForm
    template_name = 'crearCLEI.html'
    success_url = '/clei/list'

class CLEIListView(LoginRequiredMixin, SuperuserRequiredMixin, ListView):
    model = CLEI
    context_object_name = 'cleis'
    template_name = 'listarCLEI.html'

class CLEIUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    model = CLEI
    template_name = 'actualizarCLEI.html'
    success_url = '/clei/list'

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
