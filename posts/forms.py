from django import forms
from posts.models import Posts

class PostCreateForm(forms.ModelForm):
    class Meta: #estamos mudando as caracteristicas da classe META que JA EXISTE no django
        model = Posts
        fields = ['autor','categorias','texto'] 
        #em fields colocamos os valores de entrada que criamos em models.py
        #não precisa do created_at pois ja é automático