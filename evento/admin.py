from django.contrib import admin
from evento.models import Lugar, Evento, Charla, Ponencia

# Register your models here.
admin.site.register(Lugar)
admin.site.register(Evento)
admin.site.register(Charla)
admin.site.register(Ponencia)
