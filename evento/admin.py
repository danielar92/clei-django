from django.contrib import admin
from evento.models import Lugar, Taller, Charla, Ponencia, Clausura, Apertura, EventoSocial

# Register your models here.
admin.site.register(Lugar)
admin.site.register(Taller)
admin.site.register(Charla)
admin.site.register(Ponencia)
admin.site.register(Clausura)
admin.site.register(Apertura)
admin.site.register(EventoSocial)
