from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from django import forms
from django.contrib import messages
from modulo_clei.models import CLEI,Topico
from articulo.models import Evaluacion
from django.db import models
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from personas.models import Persona
from vanilla.model_views import CreateView, ListView, UpdateView, DetailView
from .utils import CLEIMixin
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin

from .forms import CLEIForm, TopicoForm, InscripcionForm

from .models import CLEI,Topico , CP, Inscripcion
from articulo.models import Articulo


def clei_processor(request):
    try:
        actual = CLEI.objects.order_by('-fechaInicio')[0]
    except IndexError:
        return {}
    inscrito = actual.inscrito(request.user) if request.user.is_authenticated() and hasattr(request.user, 'persona') else False
    return {
        'cleis': CLEI.objects.exclude(pk=actual.pk),
        'actual': actual,
        'inscrito': inscrito
    }

def home(request):
    return render(request,'home.html')


class InscripcionCreateView(LoginRequiredMixin, CLEIMixin, CreateView):
    model = Inscripcion
    form_class = InscripcionForm
    success_url = '/'
    template_name = 'crearInscripcion.html'

    def form_valid(self, form):
        inscripcion = Inscripcion(clei=self.get_clei(),
                                  persona=self.request.user.persona,
                                  costo=self.get_clei().costo_inscripcion)
        messages.success(self.request, "Inscrito exitosamente.")
        inscripcion.save()
        return HttpResponseRedirect(self.get_success_url())



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

class CLEIDetailView(DetailView):
    model = CLEI
    template_name = "detallesCLEI.html"

class CLEICreateView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = CLEI
    form_class = CLEIForm
    template_name = 'crearCLEI.html'
    success_url = '/clei/list'

    def form_valid(self, form):
        clei = form.save()
        cp = CP(clei=clei)
        cp.save()
        for miembro in form.cleaned_data['miembros']:
            cp.miembros.add(miembro)
        messages.success(self.request, "CLEI creado exitosamente.")
        return HttpResponseRedirect(self.success_url)


class CLEIListView(LoginRequiredMixin, ListView):
    model = CLEI
    context_object_name = 'cleis'
    template_name = 'listarCLEI.html'

class CLEIUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    model = CLEI
    form_class = CLEIForm
    template_name = 'actualizarCLEI.html'
    success_url = '/clei/list'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form(instance=self.object)
        form.initial['miembros'] = self.object.cp.miembros.all()
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

# # def MostrarClei(request):
#     if request.method == 'POST':
#         form = CLEIForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = CLEIForm()
# #     return render(request,'crearCLEI.html')

def evalua(request):
    if request.method == 'POST':
        formulario = EvaluarForm(request.POST)
        if formulario.is_valid():
            evaluador, created = Persona.objects.get_or_create(id=request.user.id)            
            eval = Evaluacion(articulo=formulario.cleaned_data.get('articulo'),evaluador=evaluador,nota=formulario.cleaned_data.get('nota'))
            eval.save()
    else:
        formulario = EvaluarForm()
    return render(request,'formulario.html',{'formulario':formulario}, context_instance=RequestContext(request))    
