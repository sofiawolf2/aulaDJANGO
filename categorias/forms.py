from django import forms
from categorias.models import Categorias

class CategoriasCreateForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['categorias']