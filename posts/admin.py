from django.contrib import admin

# Register your models here.

from posts.models import Posts
admin.site.register(Posts)

#acrescentamos a nossa classe POSTS nos registros do admin