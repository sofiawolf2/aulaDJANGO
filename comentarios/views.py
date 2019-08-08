from django.shortcuts import render
from comentarios.models import Comentarios
from django.views.generic import ListView
from django.urls import reverse_lazy
from comentarios.forms import ComentariosCreateForm
from django.views import generic

# Create your views here.
class ComentariosListView(ListView):
    model = Comentarios
    context_object_name = 'comentarios' #o que vamos chamar no for do html
    template_name = 'comentarios/vercom.html'
    ordering = ['-created_at']

class ComentariosCreateView(generic.CreateView):
    model = Comentarios
    form_class = ComentariosCreateForm
    template_name = 'comentarios/criarcom.html'
    success_url = reverse_lazy('comentarios:list_comentarios')

class ComentariosUpdateView(generic.UpdateView):
    model = Comentarios
    fields = ['comentario']
    template_name = 'comentarios/editcom.html'
    success_url = reverse_lazy('comentarios:list_comentarios')

class ComentariosDeletView(generic.DeleteView):
    model = Comentarios
    context_object_name = 'comentarios'
    template_name = 'comentarios/deletcom.html'
    success_url = reverse_lazy('comentarios:list_comentarios')


