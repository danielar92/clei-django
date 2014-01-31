from django.contrib import messages
from django.shortcuts import render
from evento.models import Articulo
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404

from vanilla.model_views import CreateView, ListView, UpdateView, DetailView
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin

from .models import Articulo
from .forms import ArticuloForm


from modulo_clei.utils import CLEIMixin


# Create your views here.
def articulo(request):
	if request.method=='POST':
		formulario = ArticuloForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		return render_to_response('formulario.html',{'formulario':formulario}, context_instance=RequestContext(request))

class ArticuloCreateView(LoginRequiredMixin, CLEIMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'crearArticulo.html'
    success_url = '/clei/articulos/list'
    clei = None

    def form_valid(self, form):
        self.object = form.save()
        clei = self.get_clei()
        self.object.clei = clei
        self.object.save()
        messages.success(self.request, "Articulo guardado exitosamente. Sera evaluado a la brevedad.")
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



# Create your views here.
