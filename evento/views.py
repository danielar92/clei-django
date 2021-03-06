from django.shortcuts import render
from evento.forms import LugarForm, CharlaForm, TallerForm, PonenciaForm, ClausuraForm, AperturaForm, EventoSocialForm
from evento.models import Lugar, Charla
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# Create your views here.
def lugar(request):
	if request.method=='POST':
		formulario = LugarForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = LugarForm()
	return render_to_response('eventos/formLugar.html',{'formulario':formulario}, context_instance=RequestContext(request))
	
def taller(request):
	if request.method=='POST':
		formulario = TallerForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = TallerForm()
	return render_to_response('eventos/formTaller.html',{'formulario':formulario}, context_instance=RequestContext(request))

def charla(request):
	if request.method=='POST':
		formulario = CharlaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = CharlaForm()
	return render_to_response('eventos/formCharla.html',{'formulario':formulario}, context_instance=RequestContext(request))
	
def ponencia(request):
	if request.method=='POST':
		formulario = PonenciaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = PonenciaForm()
	return render_to_response('eventos/formPonencia.html',{'formulario':formulario}, context_instance=RequestContext(request))
	
def clausura(request):
	if request.method=='POST':
		formulario = ClausuraForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = ClausuraForm()
	return render_to_response('eventos/formClausura.html',{'formulario':formulario}, context_instance=RequestContext(request))
	
def apertura(request):
	if request.method=='POST':
		formulario = AperturaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = AperturaForm()
	return render_to_response('eventos/formApertura.html',{'formulario':formulario}, context_instance=RequestContext(request))
	
def evesocial(request):
	if request.method=='POST':
		formulario = EventoSocialForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = EventoSocialForm()
	return render_to_response('eventos/formEvesocial.html',{'formulario':formulario}, context_instance=RequestContext(request))
