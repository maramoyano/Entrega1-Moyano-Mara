from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Profesor, Estudiante
from .forms import CrearCursoForm, CrearProfesorForm, CrearEstudiantesForm


# Create your views here.
def mostrar_curso(request):
    curso = Curso(nombre='Tercer anio', division='b')

    saludo = f'Hola a la todos, este es el curso de {curso.nombre}, de la division: {curso.division}'

    return HttpResponse(saludo)
    #return render(request, '', {'nombre': curso.nombre, 'division': curso.division})

def mostrar_index(request):

    return render(request, 'index.html')


def crear_curso(request):


    if request.method == 'POST':

        formulario = CrearCursoForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            curso = Curso(nombre=formulario_limpio['nombre'], division=formulario_limpio['division'])

            curso.save()

            return render(request, 'index.html')

    else:
        formulario = CrearCursoForm()

    return render(request, 'crear_curso.html', {'formulario': formulario})


def crear_profesor(request):

    if request.method == 'POST':

        formulario = CrearProfesorForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            profesor = Profesor(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], email=formulario_limpio['email'], profesion=formulario_limpio['profesion'])

            profesor.save()

            return render(request, 'index.html')

    else:
        formulario = CrearProfesorForm()
    return render(request, 'crear_profesor.html', {'formulario': CrearProfesorForm})



def buscar_profesor(request):

    if request.GET.get('email', False):
        email = request.GET['email']
        profesores = Profesor.objects.filter(email__icontains=email)

        return render(request, 'buscar_profesor.html', {'profesores': profesores})
    else:
        respuesta = 'No hay datos'
    return render(request, 'buscar_profesor.html', {'respuesta': respuesta})


def crear_estudiantes(request):
    if request.method == 'POST':

        formulario = CrearEstudiantesForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            Estudiante = Estudiante(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], email=formulario_limpio['email'], curso=formulario_limpio['curso'], institucion=formulario_limpio['institucion'])

            Estudiante.save()

            return render(request, 'index.html')

    else:
        formulario = CrearEstudiantesForm()
    return render(request, 'crear_estudiantes.html', {'formulario': CrearEstudiantesForm})