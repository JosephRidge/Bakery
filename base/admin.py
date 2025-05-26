from django.contrib import admin

# import models
from .models import Customer, Recipe, Shop , Author, Comment, Post

# Register your models here.
admin.site.register(Customer)
admin.site.register(Recipe)
admin.site.register(Shop)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Post)