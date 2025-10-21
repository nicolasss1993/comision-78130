from django.db import models
import uuid


def generar_code():
    return uuid.uuid4().hex


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    nro_comision = models.IntegerField(unique=True)
    code = models.CharField(
        max_length=32,
        unique=True,
        default=generar_code
    )
    
    def __str__(self):
        return f"{self.nombre} - Nro: {self.nro_comision}"

