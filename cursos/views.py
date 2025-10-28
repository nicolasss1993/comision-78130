from cursos.forms import CursoForm
from cursos.models import Curso
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'cursos/curso_list.html'
    context_object_name = "cursos"
    
    def get_queryset(self):
        query = self.request.GET.get("q", '')
        if query:
            return Curso.objects.filter(nombre=query).order_by("-fecha_creacion")
        return Curso.objects.all()


class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = "cursos/curso_form.html"
    success_url = reverse_lazy('curso_list') # redirect


class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = "cursos/curso_form.html"
    success_url = reverse_lazy('curso_list')
    slug_field = 'code'
    slug_url_kwarg = 'code'


class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = "cursos/cursos_confirm_delete.html"
    success_url = reverse_lazy('curso_list')
    slug_field = 'nro_comision'
    slug_url_kwarg = 'nro_comision'


class CursoDetailView(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "cursos/curso_detail.html"
    context_object_name = "curso"
    slug_field = "code"
    slug_url_kwarg = "code"
