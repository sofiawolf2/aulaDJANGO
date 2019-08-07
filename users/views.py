from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from users.models import User

# Create your views here.

class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/list.html'
