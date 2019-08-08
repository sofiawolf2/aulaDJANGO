from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from users.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin 
# LoginRequiredMixin é uma condição pra so fazer o que quer se estiver logado antes
from django.urls import reverse_lazy
from users.forms import UserCreateForm

# Create your views here.

class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/list.html'
class UserLoginViews(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass 

class UserCadastroView( generic.CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/cadastro.html'
    success_url = reverse_lazy('users:cadastro_user')

class UserSobreView(LoginRequiredMixin, generic.DetailView):
    model = User
    context_object_name = 'users'
    template_name = 'users/sobre.html'
    success_url = reverse_lazy('users:sobre_user')
    

    

