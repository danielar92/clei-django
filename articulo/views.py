from django.shortcuts import render
from evento.models import Articulo
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import CreateView, ListView, UpdateView
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin


from articulo.forms import ArticuloForm

# Create your views here.
def articulo(request):
	if request.method=='POST':
		formulario = ArticuloForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = ArticuloForm()
	return render_to_response('formulario.html',{'formulario':formulario}, context_instance=RequestContext(request))
