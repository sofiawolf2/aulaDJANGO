from django.urls import path
from posts.views import PostListView, PostCreateView, PostUpdateView, PostDeletView

#sabe quando vc vai na barra la em cima de pesquisa? www......
#Pronto. aqui criaremos a palavra que será usada depois de / para acessar o html desejado

#Lembra de quando usamos o comando URL no html pra linkar com algo (redirecionar)?
#Pronto. Aqui também é onde definimos o 'nome' desses urls para linkarmos no html base

app_name = 'posts' # relacionando com o app de 'MY APPS' do settings.py

urlpatterns = [
    #comando padrão:
    #path('palavra da barra de pesquisa', comando_criado_por_vc_no_views.as_view(),name = 'urls do base.html'),
    path('posts', PostListView.as_view(),name = 'posts_posts'),
    # definimos o que temos que escrever na barra de pesquisa pra acessar posts (\posts)
    # e também definimos o nome ('name') que usaremos  no html base para acessar esse \posts (posts_posts)
    path('novopost',PostCreateView.as_view(),name = 'novo_post'),
    path('post/<int:pk>/edit', PostUpdateView.as_view(),name = 'edit_post'),
    path('post/<int:pk>/delet',PostDeletView.as_view(),name = 'delet_post'),
]

