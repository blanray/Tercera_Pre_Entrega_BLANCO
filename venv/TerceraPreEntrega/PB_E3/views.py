from django.shortcuts import render, redirect

# Create your views here.

from .models import *

def inicio(request):
    return render(request, 'PB_E3/inicio.html')

def cursos(request):

    if request.method == 'POST':

        misId = 0
        
        try:
            misId = Curso.objects.latest('id')
        except :
            pass

        if misId == 0:
            nuevoId = 1
        else:
            nuevoId = misId.id + 1

        curso = Curso(nuevoId,request.POST['nombreCurso'], request.POST['numeroCamada'])
        curso.save()
        return redirect('cursos')


    
    cursos = Curso.objects.all()

    return render(request, 'PB_E3/cursos.html', {'cursos': cursos})

def profesores(request):

    profesores = Profesor.objects.all()

    return render(request, 'PB_E3/profesores.html', {'profesores': profesores})

def estudiantes(request):

    estudiantes = Estudiante.objects.all()

    return render(request, 'PB_E3/estudiantes.html', {'estudiantes': estudiantes})

def entregables(request):

    entregables = Entregable.objects.all()

    return render(request, 'PB_E3/entregables.html', {'entregables':entregables})



