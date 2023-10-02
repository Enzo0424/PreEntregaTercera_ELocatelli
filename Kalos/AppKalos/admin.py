from django.contrib import admin
from .models import Pacientes, Profesionales, Consultorios, Tratamientos
# Register your models here.

admin.site.register(Pacientes)
admin.site.register(Profesionales)
admin.site.register(Consultorios)
admin.site.register(Tratamientos)