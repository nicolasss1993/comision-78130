from django import forms
from cursos.models import Curso


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nombre", "nro_comision"]
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "nro_comision": forms.NumberInput(attrs={'class': 'form-control'})
        }
