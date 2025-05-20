from django.urls import path
from . import views

urlpatterns = [ 
       path('login/',views.loginUser, name='login'), 
       path('',views.home, name='home'), 
       path('recipes/',views.recipes, name='recipes'), 
       path('recipe/<str:pk>/',views.recipe, name='recipe'),
       path('create-recipe/',views.createRecipe, name='create-recipe'),
       path('update-recipe/<str:pk>/',views.updateRecipe, name='update-recipe'),
       path('cart/',views.cart, name='cart'),
       path('my-shop/',views.shop, name='shop'),
       path('shop/create-shop/',views.createShop, name='create-shop'),
       path('about/',views.about, name='about'),
]
