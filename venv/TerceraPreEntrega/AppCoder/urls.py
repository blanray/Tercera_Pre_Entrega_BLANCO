from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio),
    path('cursos', views.cursos, name = 'cursos'),
    path('profesores', views.profesores),
    path('estdiantes', views.estudiantes),
    path('entregables', views.entregables),

]
