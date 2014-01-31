from django.contrib import admin
from personas.models import Persona, Autor, MiembroCP

# Register your models here.
admin.site.register(Persona)
admin.site.register(Autor)
admin.site.register(MiembroCP)
