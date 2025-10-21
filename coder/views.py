from django.shortcuts import render, redirect, get_object_or_404
from coder.forms import *
from coder.models import Estudiante
from django.contrib import messages

def index(request):
    return render(request, "coder/index.html")


def test(request):
    return render(request, "coder/test.html")


def crear_estudiante(request):
    # GET - Pedir informacion a la base de datos.
    # POST - Solicitud para crear informacion/manipular informacion.
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiante_form")
    else:
        form = EstudianteForm()
    
    return render(request, "coder/estudiante_form.html", {'form': form})

def lista_estudiantes(request):
    query = request.GET.get('q', '')
    if len(query) > 0: # if query:
        estudiante = Estudiante.objects.filter(
            nombre__icontains=query).order_by("-fecha_de_creacion")
    else:
        estudiante = Estudiante.objects.all().order_by("-fecha_de_creacion")
    
    return render(request, "coder/estudiante_list.html", {"estudiantes": estudiante, "query": query})


def eliminar_estudiante(request, nro_legajo): # pk = ID en la base de datos
    #try: except:
    #estudiante = Estudiante.objects.get(nombre=pk)  # Si este metodo me devuelve 2 o mas registro - ROMPE MultipleObjectObtain
    estudiante = get_object_or_404(Estudiante, nro_legajo=nro_legajo)   # Si no existe ningun registro con ese nombre - ERROR- DoesNotExist.
    estudiante.delete()
    messages.success(request, "Estudiante eliminado correctamente")
    return redirect('estudiante_list')


def modificar_estudiante(request, nro_legajo):
    estudiante = get_object_or_404(Estudiante, nro_legajo=nro_legajo)
    if request.method == "POST":
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect("estudiante_list")
    else:
        form = EstudianteEditForm(instance=estudiante) # Esto es para limitar campos en la edicion
    
    return render(request, "coder/estudiante_form.html", {'form': form, 'edicion': True})
