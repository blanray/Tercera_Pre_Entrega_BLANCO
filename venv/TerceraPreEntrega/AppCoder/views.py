from django.shortcuts import render, redirect

# Create your views here.

from .models import *

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):

    if request.method == 'POST':

        misId = Curso.objects.latest('id')
        nuevoId = misId.id + 1

        curso = Curso(nuevoId,request.POST['nombreCurso'], request.POST['numeroCamada'])
        curso.save()
        return redirect('cursos')


    
    cursos = Curso.objects.all()

    return render(request, 'AppCoder/cursos.html', {'cursos': cursos})

def profesores(request):

    profesores = Profesor.objects.all()

    return render(request, 'AppCoder/profesores.html', {'profesores': profesores})

def estudiantes(request):

    estudiantes = Estudiante.objects.all()

    return render(request, 'AppCoder/estudiantes.html', {'estudiantes': estudiantes})

def entregables(request):

    entregables = Entregable.objects.all()

    return render(request, 'AppCoder/entregables.html', {'entregables':entregables})



