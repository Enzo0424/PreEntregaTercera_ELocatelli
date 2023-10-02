from django.shortcuts import render
from django.http import HttpResponse
from AppKalos.models import Pacientes, Profesionales, Consultorios,Tratamientos
from AppKalos.forms import PacienteFormulario, BuscarPaciente

# Create your views here.
def inicio(request):
    return render(request, "AppKalos/index.html") #lo mas avanzado hasta ahora

def paciente(request):
    return render (request, "AppKalos/pacientes.html")

def profesional(request):
    return render (request, "AppKalos/profesionales.html")

def consultorio(request):
    return render (request, "AppKalos/consultorios.html")

def tratamiento(request):
    return render (request, "AppKalos/tratamientos.html")

def pacientes_form(request):
    if request.method == "POST": #camino del POST
 
            miFormulario = PacienteFormulario(request.POST) # Aqui me llega la informacion del html
 
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                paciente = Pacientes(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"])
                paciente.save()
                return render(request, "AppKalos/index.html")
    else: #camino del GET
            miFormulario = PacienteFormulario()
 
    return render(request, "AppKalos/pacientesForm.html", {"miFormulario": miFormulario})


    
    respuesta = f"Estoy buscando al paciente {request.GET['nombre']}"
    
    return HttpResponse(respuesta)

def buscar_pacientes(request):
    if request.method == "POST": #camino del POST
 
        miFormulario = BuscarPaciente(request.POST) # Aqui me llega la informacion del html
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            pacientes = Pacientes.objects.filter(dni__icontains=informacion["dni"])
                
            return render(request, "AppKalos/buscarpacientes.html", {"pacientes":pacientes})
    else: #camino del GET
            miFormulario = BuscarPaciente() 
 
    return render(request, "AppKalos/pacientesApi.html", {"miFormulario":miFormulario})


def mostrar_pacientes(request):
    pass