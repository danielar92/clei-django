from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login

from registration import signals
from registration.backends.simple.views import RegistrationView

from .forms import PersonaForm
from .models import Persona
from modulo_clei.models import CLEI
# Create your views here.

class PersonaRegistrationView(RegistrationView):
    form_class = PersonaForm

    def register(self, request, **cleaned_data):
        username, email, password = cleaned_data['username'], cleaned_data['email'], cleaned_data['password1']
        nombre, apellido, institucion = cleaned_data['nombre'], cleaned_data['apellido'], cleaned_data['institucion']
        pais, experticies = cleaned_data['pais'], cleaned_data['experticies']
        dirPostal,pagWeb,telf = cleaned_data['dirPostal'],cleaned_data['pagWeb'],cleaned_data['telf']
        Persona.objects._create_user(username, email, password, False, False,
                                     nombre=nombre, apellido=apellido,
                                     institucion=institucion, pais=pais,dirPostal=dirPostal,pagWeb=pagWeb,telf=telf)
        new_user = authenticate(username=username, password=password)
        for experticie in experticies:
            new_user.persona.experticies.add(experticie)
        login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)


        return new_user
