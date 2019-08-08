from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from posts.models import Posts
from posts.forms import PostCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
# LoginRequiredMixin é uma condição pra so fazer o que quer se estiver logado antes

# Create your views here.

class PostListView(ListView):
    model = Posts
    context_object_name = 'posts'
    template_name = 'posts/posts.html'
    ordering = ['-created_at']

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Posts
    form_class = PostCreateForm
    template_name = 'posts/novo.html'
    success_url = reverse_lazy('posts:novo_post')
    #apos ter sucesso(enviar o poste, nesse caso), a pag sera redirecionado para 'novo_post' novamente

class PostUpdateView(LoginRequiredMixin ,generic.UpdateView):
    model = Posts
    fields = ['autor','categorias','texto']
    template_name = 'posts/edit.html'
    success_url = reverse_lazy('posts:posts_posts')

class PostDeletView(LoginRequiredMixin ,generic.DeleteView):
    model = Posts
    context_object_name = 'post' #faz coneção com o 'post' do for.
    #ta no singular pq vamos excluir um post por vez
    template_name= 'posts/delet.html'
    success_url = reverse_lazy('posts:posts_posts')


