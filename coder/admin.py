from django.contrib import admin
from coder.models import *


#admin.site.register(Estudiante)


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista del modelo
    list_display = ("nombre", "apellido", "nro_legajo", "fecha_de_nacimiento")
    # Columnas con enlaces clickeables para entrar al detalle
    list_display_links = ("nombre", "apellido")
    # Campos por los que se puede buscar
    search_fields = ("nro_legajo",) # ("nro_legajo",)
    # Filtros laterales
    list_filter = ("fecha_de_nacimiento", "fecha_de_creacion")
    # Orden por defecto
    ordering = ("apellido", "nombre", "nro_legajo")
    # Campos de solo lectura
    readonly_fields = ("fecha_de_creacion",)

