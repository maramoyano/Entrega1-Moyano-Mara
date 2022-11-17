from django import forms

class CrearCursoForm(forms.Form):

    nombre = forms.CharField()
    division = forms.IntegerField()


class CrearProfesorForm(forms.Form):

    nombre = forms.CharField(min_length=5, max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    asignatura = forms.CharField(max_length=40)
