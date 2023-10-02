from django import forms

class PacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    
class BuscarPaciente(forms.Form):
    dni = forms.IntegerField()
    
    
    