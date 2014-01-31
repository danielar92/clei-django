from django.contrib import admin
from modulo_clei.models import CLEI, Topico, Inscripcion, Evaluacion

# Register your models here.
admin.site.register(CLEI)
admin.site.register(Topico)
admin.site.register(Inscripcion)
admin.site.register(Evaluacion)