from django.shortcuts import render
from django.views import generic
from categorias.models import Categorias
from django.views.generic import ListView
from django.urls import reverse_lazy

# Create your views here.

class CategoriasListView(ListView):
    model = Categorias
    context_object_name = 'categorias'
    #template_name = 'posts/posts.html'
    ordering = ['-created_at']

class CategoriasCreateView(generic.CreateView):
    model = Categorias
    # form_class = CategoriaCreateForm
    template_name = 'categorias/criar.html'
    success_url = reverse_lazy('posts:posts_posts')
