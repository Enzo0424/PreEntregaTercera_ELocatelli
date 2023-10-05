from django import forms

class PacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    
class BuscarPaciente(forms.Form):
    dni = forms.IntegerField()
    
class BuscarProfesional (forms.Form):
    profesion = forms.CharField(max_length=30)

class CargarProfesional (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    profesion = forms.CharField(max_length=30)

class CargarConsultorios (forms.Form):
    nombre = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=30)
    
class CargarTratamientos (forms.Form):
    codigo = forms.CharField(max_length=4)
    descripcion = forms.CharField(max_length=30)