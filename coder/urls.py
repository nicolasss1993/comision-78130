from django.urls import path
from .views import index, test, crear_estudiante, lista_estudiantes, eliminar_estudiante, modificar_estudiante

urlpatterns = [
    path("", index, name="index"),
    path("test/", test , name="test"),
    path("estudiantes/nuevo", crear_estudiante, name="estudiante_form"),
    path("estudiantes/", lista_estudiantes, name="estudiante_list"),
    path("estudiante/<int:nro_legajo>/eliminar", eliminar_estudiante, name="eliminar_estudiante" ),
    path("estudiante/<int:nro_legajo>/modificar", modificar_estudiante, name="modificar_estudiante")
]