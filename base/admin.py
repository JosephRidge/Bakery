from django.contrib import admin

# import models
from .models import Customer, Recipe

# Register your models here.
admin.site.register(Customer)
admin.site.register(Recipe)