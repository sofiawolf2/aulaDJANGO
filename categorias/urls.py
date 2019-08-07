from django.urls import path
from categorias.views import CategoriasListView, CategoriasCreateView, CategoriasDeletView, CategoriasUpdateView

app_name = 'categorias'

urlpatterns = [
    path('categorialist',CategoriasListView.as_view(),name = 'list_categorias'),
    path('criarcategorias',CategoriasCreateView.as_view(),name = 'criar_categorias'),
    path('categoria/<int:pk>/edit',CategoriasUpdateView.as_view(),name = 'edit_categorias'),
    path('categoria/<int:pk>/delet',CategoriasDeletView.as_view(),name = 'delet_categorias'),

]
