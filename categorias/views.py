from django.shortcuts import render
from django.views import generic
from categorias.models import Categorias
from django.views.generic import ListView
from django.urls import reverse_lazy
from categorias.forms import CategoriasCreateForm


# Create your views here.

class CategoriasListView(ListView):
    model = Categorias
    context_object_name = 'categorias'
    template_name = 'categoria/listc.html'

class CategoriasCreateView(generic.CreateView):
    model = Categorias
    form_class = CategoriasCreateForm
    template_name = 'categoria/criar.html'
    success_url = reverse_lazy('categorias:list_categorias')

class CategoriasUpdateView(generic.UpdateView):
    model = Categorias
    fields = ['categorias']
    template_name = 'categoria/editc.html'
    success_url = reverse_lazy('categorias:list_categorias')

class CategoriasDeletView(generic.DeleteView):
    model = Categorias
    context_object_name = 'categorias' #faz coneção com o 'post' do for.
    #ta no singular pq vamos excluir um post por vez
    template_name= 'categoria/excluir.html'
    success_url = reverse_lazy('categorias:list_categorias')
