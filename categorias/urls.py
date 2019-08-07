from django.urls import path
from categorias.views import CategoriasListView, CategoriasCreateView

app_name = 'categorias'

urlpatterns = [
    path('categorias/criar', CategoriasCreateView.as_view(),name = 'criar_categorias'),
]
