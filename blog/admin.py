from django.contrib import admin
from .models import Post, Comment

'''Чтобы наша модель стала доступна на странице 
   администрирования, нам нужно 
   зарегистрировать её'''

admin.site.register(Post)
admin.site.register(Comment)
