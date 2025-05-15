from django.contrib import admin

# import models
from .models import Customer, Recipe, Shop

# Register your models here.
admin.site.register(Customer)
admin.site.register(Recipe)
admin.site.register(Shop)