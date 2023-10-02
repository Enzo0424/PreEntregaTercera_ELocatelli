from django.urls import path
from AppKalos.views import inicio, paciente, profesional, consultorio, tratamiento, pacientes_form,buscar_pacientes,mostrar_pacientes


urlpatterns = [
    path('Inicio/', inicio, name= "Inicio"),
    path('Pacientes/', paciente, name="Pacientes"),
    path('Profesionales/', profesional, name="Profesionales"),
    path('Consultorios/', consultorio, name="Consultorios"),
    path('Tratamientos/', tratamiento, name="Tratamientos"),
    path('Pacientesform/', pacientes_form, name="Carga de Pacientes"),
    path('Buscar_Pacientes/', buscar_pacientes, name="Buscar Pacientes"),
    path('Mostrar_Pacientes/', mostrar_pacientes, name="Mostrar Pacientes"),
]