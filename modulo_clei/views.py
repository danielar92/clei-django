from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from django import forms
from modulo_clei.models import CLEI,Topico , CP, Articulo
from django.db import models
from django.http import HttpResponseRedirect
from django.forms import ModelForm

from vanilla.model_views import CreateView, ListView, UpdateView, DetailView
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin


from .forms import CLEIForm, TopicoForm, ArticuloForm


def log_in_processor(request):
    return {'login_form': AuthenticationForm()}

def home(request):
    return render(request,'home.html')

# class CPCreateView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
#     model = CP
#     form_class = CPForm
#     template_nema = 'crearCP.html'
#     succes_url = '/clei/CP/create'


class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'crearArticulo.html'
    success_url = '/clei/articulos/list'

    def form_valid(self, form):
        self.object = form.save()
        clei_pk = self.kwargs.get('pk')
        clei = CLEI.objects.get(pk=clei_pk)
        self.object.clei = clei
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ArticuloListView(LoginRequiredMixin, ListView):
    model = Articulo
    context_object_name = 'articulos'
    template_name = 'listarArticulos.html'
    def get_queryset(self):
        return self.request.user.persona.articulos.all()

class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    template_name = 'actualizarArticulo.html'
    success_url = '/clei/articulos/list'


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

# def MostrarClei(request):
#     return render(request,'crearCLEI.html')

# def CrearClei(request):
#     if request.method == 'POST':
#         form = CLEIForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = CLEIForm()
#     return render(request,'crearCLEI.html',{'cleiform':form})
