from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name = 'index'),
    path('cursos', views.cursos, name = 'cursos'),
    path('profesores', views.profesores, name = 'profesores'),
    path('estudiantes', views.estudiantes, name = 'estudiantes'),
    path('entregables', views.entregables, name = 'entregables'),
    path('editar/<miIdMain>/', views.editar, name = 'editar'),
]

cursos = [
    path('eliminarCurso/<idCurso>/', views.eliminarCurso, name = 'eliminarCurso'),
    path('editarCurso/<idCurso>/', views.editarCurso, name = 'editarCurso'),
]

profesores = [
    path('eliminarProfesor/<idProfesor>/', views.eliminarProfesor, name = 'eliminarProfesor'),
    path('editarProfesor/<idProfesor>/', views.editarProfesor, name = 'editarProfesor'),
]

estudiantes = [
    path('eliminarEstudiante/<idEstudiante>/', views.eliminarEstudiante, name = 'eliminarEstudiante'),
    path('editarEstudiante/<idEstudiante>/', views.editarEstudiante, name = 'editarEstudiante'),
]

entregables = [
    path('eliminarEntregabe/<idEntregable>/', views.eliminarEntregable, name = 'eliminarEntregable'),
    path('editarEntregable/<idEntregable>/', views.editarEntregable, name = 'editarEntregable'),
]

urlpatterns += cursos

urlpatterns += profesores

urlpatterns += estudiantes

urlpatterns += entregables