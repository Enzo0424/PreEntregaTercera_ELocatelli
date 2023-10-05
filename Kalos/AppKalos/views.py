from django.shortcuts import render
from django.http import HttpResponse
from AppKalos.models import Pacientes, Profesionales, Consultorios,Tratamientos
from AppKalos.forms import PacienteFormulario, BuscarPaciente, BuscarProfesional, CargarConsultorios, CargarTratamientos,CargarProfesional
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

def pacientes_form(request): #carga pacientess
    if request.method == "POST": #camino del POST
 
            miFormulario = PacienteFormulario(request.POST) # Aqui me llega la informacion del html
 
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                paciente = Pacientes(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"])
                paciente.save()
                return render(request, "AppKalos/pacientes.html")
    else: #camino del GET
            miFormulario = PacienteFormulario()
 
    return render(request, "AppKalos/cargarPaciente.html", {"miFormulario": miFormulario})    

def buscar_pacientes(request):
    if request.method == "POST": #camino del POST
 
        miFormulario = BuscarPaciente(request.POST) # Aqui me llega la informacion del html
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            pacientes = Pacientes.objects.filter(dni__icontains=informacion["dni"])
                
            return render(request, "AppKalos/mostrarpacientes.html", {"pacientes":pacientes})
    else: #camino del GET
            miFormulario = BuscarPaciente() 
 
    return render(request, "AppKalos/buscarpaciente.html", {"miFormulario":miFormulario})

def buscar_profesional(request):
    if request.method == "POST": #camino del POST
 
        miFormulario = BuscarProfesional(request.POST) # Aqui me llega la informacion del html
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesionales = Profesionales.objects.filter(profesion__icontains=informacion["profesion"])
                
            return render(request, "AppKalos/mostrarprofesional.html", {"profesionales":profesionales})
    else: #camino del GET
            miFormulario = BuscarProfesional() 
 
    return render(request, "AppKalos/buscarProfesional.html", {"miFormulario":miFormulario})

def cargar_consultorio(request): #carga pacientess
    if request.method == "POST": #camino del POST
 
            miFormulario = CargarConsultorios(request.POST) # Aqui me llega la informacion del html
 
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                consultorio = Consultorios(nombre=informacion["nombre"], direccion=informacion["direccion"])
                consultorio.save()
                return render(request, "AppKalos/consultorios.html")
    else: #camino del GET
            miFormulario = CargarConsultorios()
 
    return render(request, "AppKalos/cargarConsultorio.html", {"miFormulario": miFormulario}) 

def cargar_tratamiento(request): #carga pacientess
    if request.method == "POST": #camino del POST
 
            miFormulario = CargarTratamientos(request.POST) # Aqui me llega la informacion del html
 
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                tratamiento = Tratamientos(codigo=informacion["codigo"], descripcion=informacion["descripcion"])
                tratamiento.save()
                return render(request, "AppKalos/tratamientos.html")
    else: #camino del GET
            miFormulario = CargarTratamientos()
 
    return render(request, "AppKalos/cargarTratamientos.html", {"miFormulario": miFormulario})

def cargar_profesional(request): #carga pacientess
    if request.method == "POST": #camino del POST
 
            miFormulario = CargarProfesional(request.POST) # Aqui me llega la informacion del html
 
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                profesional = Profesionales(nombre=informacion["nombre"], apellido=informacion["apellido"], profesion=informacion["profesion"])
                profesional.save()
                return render(request, "AppKalos/profesionales.html")
    else: #camino del GET
            miFormulario = CargarProfesional()
 
    return render(request, "AppKalos/cargarProfesional.html", {"miFormulario": miFormulario})
