# se configura la vista 
from django.shortcuts import render, redirect
from .forms import ProfesorForm, EstudianteForm, CursoForm
from .models import Profesor, Estudiante, Curso

def home(request):
    return render(request, 'app/home.html')

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfesorForm()
    return render(request, 'app/agregar_profesor.html', {'form': form})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EstudianteForm()
    return render(request, 'app/agregar_estudiante.html', {'form': form})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CursoForm()
    return render(request, 'app/agregar_curso.html', {'form': form})

def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        profesores = Profesor.objects.filter(nombre__icontains=query)
        estudiantes = Estudiante.objects.filter(nombre__icontains=query)
        cursos = Curso.objects.filter(nombre__icontains=query)
        return render(request, 'app/buscar.html', {
            'profesores': profesores,
            'estudiantes': estudiantes,
            'cursos': cursos
        })
    return render(request, 'app/buscar.html')
