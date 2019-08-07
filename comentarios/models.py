from django.db import models

# Create your models here.
class Comentarios(models.Model):
    post = models.ForeignKey("posts.Posts",verbose_name = 'post', on_delete = models.CASCADE)
    comentario = models.TextField(verbose_name = 'comentario')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Comentario {self.pk}'
