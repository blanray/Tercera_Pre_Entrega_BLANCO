from django.db import models

# Create your models here.

class Curso(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f'Curso | Id: {self.id} - Nombre: {self.nombre} - Camada: {self.camada}'

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f'Estudiante | Id: {self.id} - Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}'

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f'Profesor | Id: {self.id} - Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesion: {self.profesion}'

class Entregable(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f'Entrergable | Id: {self.id} - Nombre: {self.nombre} - Fecha de Entrega: {self.fechaDeEntrega} - Entregado: {self.entregado}'
