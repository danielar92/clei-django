from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
from modulo_clei.views import CLEICreateView, CLEIListView, CLEIUpdateView, TopicoCreateView, TopicoListView, TopicoUpdateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'modulo_clei.views.home', name='home'),
    (r'^accounts/', include('registration.backends.simple.urls')),
    (r'^users/(?P<username>\w+)/', RedirectView.as_view(url='/')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^clei/create/$', CLEICreateView.as_view(),name='clei_create'),
	url(r'^clei/list/$', CLEIListView.as_view(),name='clei_list'),
	url(r'^clei/update/(?P<pk>\d+)/$', CLEIUpdateView.as_view(),name='clei_update'),
	url(r'^clei/topicos/create/$', TopicoCreateView.as_view(),name='clei_topico_create'),
	url(r'^clei/topicos/list/$', TopicoListView.as_view(),name='clei_topico_list'),
	url(r'^clei/topicos/update/(?P<pk>\d+)/$', TopicoUpdateView.as_view(),name='clei_topico_update'),
    # Eventos
    url(r'^lugar/$','evento.views.lugar'),
    url(r'^taller/$','evento.views.taller'),
    url(r'^ponencia/$','evento.views.ponencia'),
    url(r'^charla/$','evento.views.charla'),
    url(r'^apertura/$','evento.views.apertura'),
    url(r'^clausura/$','evento.views.clausura'),
    url(r'^evesocial/$','evento.views.evesocial'),
)
