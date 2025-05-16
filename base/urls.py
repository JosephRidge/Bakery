from django.urls import path
from . import views

urlpatterns = [
       path('home/',views.home, name='home'),
       path('recipes/',views.recipes, name='recipes'), 
       path('recipe/<str:pk>/',views.recipe, name='recipe'),
       path('create-recipe/',views.createRecipe, name='create-recipe'),
       path('cart/',views.cart, name='cart'),
       path('shop/',views.shop, name='shop'),
       path('about/',views.about, name='about'),
]
