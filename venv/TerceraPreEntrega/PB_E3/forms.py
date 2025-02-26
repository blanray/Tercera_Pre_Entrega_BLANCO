from django import forms

class CursoFormulario(forms.Form):
    id = forms.HiddenInput()
    curso = forms.CharField(min_length=1, max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nombre del curso (1 a 30 caracteres)',
        }
    ))
    camada = forms.IntegerField(min_value=1, max_value=99999, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Numero de camada (1 a 99999)',
        }
    ))

class ProfesorFormulario(forms.Form):
    id = forms.HiddenInput()
    nombre = forms.CharField(min_length=1, max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nombre del profesor (1 a 30 caracteres)',
        }
    ))
    apellido = forms.CharField(min_length=1, max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Apellido del profesor (1 a 30 caracteres)',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email del profesor (1 a 30 caracteres)',
        }
    ))
    profesion = forms.CharField(min_length=1, max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Profesion del profesor (1 a 30 caracteres)',
        }
    ))

class EstudianteFormulario(forms.Form):
    id = forms.HiddenInput()
    nombre = forms.CharField(min_length=1, max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nombre del estudiante (1 a 30 caracteres)',
        }
    ))
    apellido = forms.CharField(min_length=1, max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Apellido del estudiante (1 a 30 caracteres)',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email del estudiante (1 a 30 caracteres)',
        }
    ))

class EntregableFormulario(forms.Form):
    id = forms.HiddenInput()
    nombre = forms.CharField(min_length=1, max_length=30, widget=forms.TextInput(
        attrs={
        'class': 'form-control',
        'placeholder': 'Nombre del entregable (1 a 30 caracteres)',
        }
    ))
    fecha = forms.DateField(label = 'Fecha de Entrega', widget=forms.DateInput(attrs={'type':'date', 'class': 'form-control'}))
    entregado = forms.BooleanField(required=False)

class BusquedaFormulario(forms.Form):
    opciones=[
        ('curso', 'Curso'),
        ('estudiante', 'Estudiante'),
        ('profesor', 'Profesor'),
        ('entregable', 'Entregable')
    ]

    modelo = forms.ChoiceField(
        choices=opciones,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    criterio = forms.CharField(min_length=1, max_length=30, widget=forms.TextInput(
        attrs={
        'class': 'form-control',
        'placeholder': 'Criterio a buscar (1 a 30 caracteres)',
        }), help_text='Ingrese texto a buscar en nombre de Curso/Alumno/Profesor/Entregable')
