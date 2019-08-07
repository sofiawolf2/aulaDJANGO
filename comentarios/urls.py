from django.urls import path
from comentarios.views import ComentariosListView, ComentariosCreateView, ComentariosUpdateView, ComentariosDeletView

app_name = "comentarios"

urlpatterns = [
    path('comentarios', ComentariosListView.as_view(), name = 'list_comentarios'),
    path('comentarioscriar', ComentariosCreateView.as_view(), name = 'criar_comentarios'),
    path('comentarios/<int:pk>/edit', ComentariosUpdateView.as_view(), name = 'editar_comentarios'),
    path('comentarios/<int:pk>/delet', ComentariosDeletView.as_view(), name = 'delet_comentarios'),


]
