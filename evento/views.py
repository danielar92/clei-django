from django.shortcuts import render
from evento.forms import LugarForm, CharlaForm, TallerForm
from evento.models import Lugar, Charla
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# Create your views here.
def lugar(request):
	if request.method=='POST':
		formulario = CharlaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/admin')
	else:
		formulario = CharlaForm()
	return render_to_response('eventosForms.html',{'formulario':formulario}, context_instance=RequestContext(request))
