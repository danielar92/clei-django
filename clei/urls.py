from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
from modulo_clei.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'modulo_clei.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.simple.urls')),
    (r'^users/(?P<username>\w+)/', RedirectView.as_view(url='/')),
    url(r'^crearCLEI$','modulo_clei.views.MostrarClei',name='crear clei'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # Eventos
    url(r'^lugar/$','evento.views.lugar'),
)
