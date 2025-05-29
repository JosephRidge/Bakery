from django.contrib import admin
from . import views 

from django.urls import path

urlpatterns = [
       path('',views.getData),
       path('recipes/',views.getRecipes),
]
