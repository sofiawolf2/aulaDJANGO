from django.db import models
from django.contrib.auth.models import User
from categorias.models import Categorias

# Create your models here.

class Posts(models.Model):
    autor = models.ForeignKey("users.User",verbose_name = 'autor', on_delete = models.CASCADE)
    categorias = models.ForeignKey("categorias.Categorias",verbose_name = 'categorias', on_delete = models.CASCADE)
    texto = models.TextField(verbose_name = 'texto')
    created_at = models.DateTimeField(auto_now_add=True)
    #nós definimos as "entradas" que nossa classe de post terá. Ou seja, autor e texto

    def __str__(self):
        return f'postagem {self.pk} | Autor {self.autor} | Criado em {self.created_at}'
        # isso é como vai ficar o nome do arquivo no admin

    class Meta: #estamos alterando novamente as deifinições da classe META que JA EXISTE no django
        verbose_name= 'Postagem' 
        verbose_name_plural= 'Postagens'
        #dessa forma, vai mudar o nome que aparece quando acessamos o admin. 
        #quando tiver so uma postagem vai aparecer 'Postagem'
        #quando for mais de uma vai aparecer 'Postagens'

        
