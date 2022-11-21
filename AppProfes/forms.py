from django import forms

class CrearCursoForm(forms.Form):

    nombre = forms.CharField()
    division = forms.IntegerField()


class CrearProfesorForm(forms.Form):

    nombre = forms.CharField(min_length=5, max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    asignatura = forms.CharField(max_length=40)

class CrearEstudiantesForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    curso = forms.CharField(max_length=40)
    institucion = forms.CharField(max_length=40)
