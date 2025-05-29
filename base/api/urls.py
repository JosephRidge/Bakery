from django.urls import path, include
from . import views

urlpatterns = [  
       path('recipes/', views.getRecipes),
       path('shops/', views.getShops),
       path('posts/', views.getPosts), 
]
