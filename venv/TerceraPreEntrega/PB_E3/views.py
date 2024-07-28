from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import *
from .forms import *
# Create your views here.


def inicio(request):
    return render(request, 'PB_E3/inicio.html')

def cursos(request):

    if request.method == 'POST':

        miFormCursos = CursoFormulario(request.POST)

        if miFormCursos.is_valid():

            miInfo = miFormCursos.cleaned_data

            curso = Curso(nombre = miInfo['curso'], camada = miInfo['camada'])
            
            curso.save()

            messages.success(request, 'Registro agregado exitosamente')
       
        else:
            miFormCursos = CursoFormulario()
            messages.error(request, 'Error en los datos ingresados, intente nuevamente')
        
        return redirect('cursos')
         
    else:
        cursos = Curso.objects.all()
        miFormCursos = CursoFormulario()

    return render(request, 'PB_E3/cursos.html', {'cursos': cursos, 'miFormCursos': miFormCursos})

def eliminarCurso(request, idCurso):

    try:
        curso = Curso.objects.get(id=idCurso)
        curso.delete()
    except:
        pass

    return redirect(reverse('cursos'))

def editarCurso(request, idCurso):

    curso = Curso.objects.get(id=idCurso)
    miFormulario = CursoFormulario(initial={'curso' : curso.nombre, 'camada' : curso.camada})
    miIdMain = idCurso
    miEdicion = 'Curso'

    return render(request, 'PB_E3/editar.html', {'miForm': miFormulario, 'miIdMain': miIdMain, 'miEdicion': miEdicion})


def editar(request, miIdMain):

    if request.method == 'POST':
        if request.POST['miEdicion'] == 'Curso':
            miFormCursos = CursoFormulario(request.POST)
            if miFormCursos.is_valid():
                miInfo = miFormCursos.cleaned_data
                curso = Curso(id = request.POST['miIdMain'], nombre = miInfo['curso'], camada = miInfo['camada'])
                curso.save()
                messages.success(request, 'Registro actualizado exitosamente')

            else:
                messages.error(request, 'Error en los datos ingresados, intente nuevamente')

            return redirect('editarCurso', idCurso=miIdMain)

        elif request.POST['miEdicion'] == 'Profesor':
            miFormProfesores = ProfesorFormulario(request.POST)
            if miFormProfesores.is_valid():
                miInfo = miFormProfesores.cleaned_data
                profesor = Profesor(id = request.POST['miIdMain'], nombre = miInfo['nombre'], apellido = miInfo['apellido'], email = miInfo['email'], profesion = miInfo['profesion'])
                profesor.save()
                messages.success(request, 'Registro actualizado exitosamente')

            else:
                messages.error(request, 'Error en los datos ingresados, intente nuevamente')

            return redirect('editarProfesor', idProfesor=miIdMain)

        elif request.POST['miEdicion'] == 'Estudiante':
            miFormEstudiantes = EstudianteFormulario(request.POST)
            if miFormEstudiantes.is_valid():
                miInfo = miFormEstudiantes.cleaned_data
                estudiante = Estudiante(id = request.POST['miIdMain'], nombre = miInfo['nombre'], apellido = miInfo['apellido'], email = miInfo['email'])
                estudiante.save()
                messages.success(request, 'Registro actualizado exitosamente')

            else:
                messages.error(request, 'Error en los datos ingresados, intente nuevamente')

            return redirect('editarEstudiante', idEstudiante=miIdMain)

        elif request.POST['miEdicion'] == 'Entregable':
            miFormEntregables = EntregableFormulario(request.POST)
            if miFormEntregables.is_valid():
                miInfo = miFormEntregables.cleaned_data
                entregable = Entregable(id = request.POST['miIdMain'], nombre = miInfo['nombre'], fecha = miInfo['fecha'], entregado = miInfo['entregado'])
                entregable.save()
                messages.success(request, 'Registro actualizado exitosamente')

            else:
                messages.error(request, 'Error en los datos ingresados, intente nuevamente')

            return redirect('editarEntregable', idEntregable=miIdMain)


    return render(request, 'PB_E3/inicio.html')

def profesores(request):

    if request.method == 'POST':

        miFormProfesores = ProfesorFormulario(request.POST)

        if miFormProfesores.is_valid():

            miInfo = miFormProfesores.cleaned_data

            profesor = Profesor(nombre = miInfo['nombre'], apellido = miInfo['apellido'],email = miInfo['email'],profesion = miInfo['profesion'])
            
            profesor.save()

            messages.success(request, 'Registro agregado exitosamente')
       
        else:
            miFormProfesores = ProfesorFormulario()
            messages.error(request, 'Error en los datos ingresados, intente nuevamente')
        
        return redirect('profesores')
         
    else:
        profesores = Profesor.objects.all()
        miFormProfesores = ProfesorFormulario()

    return render(request, 'PB_E3/profesores.html', {'profesores': profesores, 'miFormProfesores': miFormProfesores})

def eliminarProfesor(request, idProfesor):

    try:
        profesor = Profesor.objects.get(id=idProfesor)
        profesor.delete()
    except:
        pass

    return redirect(reverse('profesores'))

def editarProfesor(request, idProfesor):

    profesor = Profesor.objects.get(id=idProfesor)
    miFormulario = ProfesorFormulario(initial={'nombre' : profesor.nombre, 'apellido' : profesor.apellido, 'email' : profesor.email, 'profesion' : profesor.profesion})
    miIdMain = idProfesor
    miEdicion = 'Profesor'

    return render(request, 'PB_E3/editar.html', {'miForm': miFormulario, 'miIdMain': miIdMain, 'miEdicion': miEdicion})

def estudiantes(request):

    if request.method == 'POST':

        miFormEstudiantes = EstudianteFormulario(request.POST)

        if miFormEstudiantes.is_valid():

            miInfo = miFormEstudiantes.cleaned_data

            estudiante = Estudiante(nombre = miInfo['nombre'], apellido = miInfo['apellido'],email = miInfo['email'])
            
            estudiante.save()

            messages.success(request, 'Registro agregado exitosamente')
       
        else:
            miFormEstudiantes = EstudianteFormulario()
            messages.error(request, 'Error en los datos ingresados, intente nuevamente')
        
        return redirect('estudiantes')
         
    else:
        estudiantes = Estudiante.objects.all()
        miFormEstudiantes = EstudianteFormulario()

    return render(request, 'PB_E3/estudiantes.html', {'estudiantes': estudiantes, 'miFormEstudiantes': miFormEstudiantes})

def eliminarEstudiante(request, idEstudiante):

    try:
        estudiante = Estudiante.objects.get(id=idEstudiante)
        estudiante.delete()
    except:
        pass

    return redirect(reverse('estudiantes'))

def editarEstudiante(request, idEstudiante):

    estudiante = Estudiante.objects.get(id=idEstudiante)
    miFormulario = EstudianteFormulario(initial={'nombre' : estudiante.nombre, 'apellido' : estudiante.apellido, 'email' : estudiante.email})
    miIdMain = idEstudiante
    miEdicion = 'Estudiante'

    return render(request, 'PB_E3/editar.html', {'miForm': miFormulario, 'miIdMain': miIdMain, 'miEdicion': miEdicion})


def entregables(request):

    if request.method == 'POST':

        miFormEntregables = EntregableFormulario(request.POST)

        if miFormEntregables.is_valid():

            miInfo = miFormEntregables.cleaned_data

            entregable = Entregable(nombre = miInfo['nombre'], fecha = miInfo['fecha'], entregado = miInfo['entregado'])
            entregable.save()

            messages.success(request, 'Registro agregado exitosamente')
       
        else:
            miFormEntregables = EntregableFormulario()
            messages.error(request, 'Error en los datos ingresados, intente nuevamente')
        
        return redirect('entregables')
         
    else:
        entregables = Entregable.objects.all()
        miFormEntregables = EntregableFormulario()

    return render(request, 'PB_E3/entregables.html', {'entregables': entregables, 'miFormEntregables': miFormEntregables})

def eliminarEntregable(request, idEntregable):

    try:
        entregable = Entregable.objects.get(id=idEntregable)
        entregable.delete()
    except:
        pass

    return redirect(reverse('entregables'))

def editarEntregable(request, idEntregable):

    entregable = Entregable.objects.get(id=idEntregable)
    miFormulario = EntregableFormulario(initial={'nombre' : entregable.nombre, 'fecha' : entregable.fecha, 'entregado' : entregable.entregado})
    miIdMain = idEntregable
    miEdicion = 'Entregable'

    return render(request, 'PB_E3/editar.html', {'miForm': miFormulario, 'miIdMain': miIdMain, 'miEdicion': miEdicion})
