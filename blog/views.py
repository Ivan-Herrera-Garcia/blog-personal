from ast import Del
#from typing_extensions import reveal_type
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Publicaciones
from django.urls import reverse_lazy

# Create your views here.
class VistaListaBlog (ListView):
    model = Publicaciones
    template_name = 'inicio.html'

class VistaDetallePublicacion(DetailView):
    model = Publicaciones
    template_name = 'detalle_publicacion.html'
    context_object_name = 'publicacion'

class VistaCrearBlog(CreateView):
    model = Publicaciones
    template_name = 'nueva_publicacion.html'
    fields = ['titulo', 'autor','cuerpo']

class VistaEditarBlog(UpdateView):
    model = Publicaciones
    template_name = "editar_publicacion.html"
    fields = ['titulo','cuerpo']

class VistaEliminarBlog(DeleteView):
    model = Publicaciones
    template_name = "eliminar_publicacion.html"
    success_url = reverse_lazy('inicio')

