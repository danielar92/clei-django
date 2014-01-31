from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
from modulo_clei.views import CLEICreateView, CLEIListView, CLEIUpdateView, CLEIDetailView, TopicoCreateView, TopicoListView, TopicoUpdateView, InscripcionCreateView
from articulo.views import  ArticuloListView, ArticuloUpdateView, ArticuloCreateView
admin.autodiscover()

from registration.backends.simple.views import RegistrationView
from personas.views import PersonaRegistrationView


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'modulo_clei.views.home', name='home'),
    url(r'^accounts/register/$',
        PersonaRegistrationView.as_view(),
        name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),

    (r'^users/(?P<username>\w+)/', RedirectView.as_view(url='/')),
                       url(r'^clei/create/$', CLEICreateView.as_view(),name='clei_create'),
                       url(r'^clei/list/$', CLEIListView.as_view(),name='clei_list'),
                       url(r'^clei/(?P<pk>\d+)/$', CLEIDetailView.as_view(),name='clei_detail'),
                       url(r'^clei/update/(?P<pk>\d+)/$', CLEIUpdateView.as_view(),name='clei_update'),
                       url(r'^clei/topicos/create/$', TopicoCreateView.as_view(),name='clei_topico_create'),
                       url(r'^clei/topicos/list/$', TopicoListView.as_view(),name='clei_topico_list'),
                       url(r'^clei/topicos/update/(?P<pk>\d+)/$', TopicoUpdateView.as_view(),name='clei_topico_update'),
                       url(r'^clei/(?P<pk>\d+)/articulos/create/$', ArticuloCreateView.as_view(),name='clei_articulo_create'),
                       url(r'^clei/(?P<pk>\d+)/inscripcion/create/$', InscripcionCreateView.as_view(),name='clei_inscripcion_create'),
                       url(r'^clei/articulos/list/$', ArticuloListView.as_view(),name='clei_articulo_list'),
                       url(r'^clei/articulos/update/(?P<pk>\d+)/$', ArticuloUpdateView.as_view(),name='clei_articulo_update'),
                       # url(r'^clei/CP/create/$', CPCreateView.as_view(),name='cp_create'),
)
