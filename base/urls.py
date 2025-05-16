from django.urls import path
from . import views

urlpatterns = [
       path('home/',views.home, name='home'),
       path('recipe/',views.recipe, name='recipe'),
       path('cart/',views.cart, name='cart'),
       path('shop/',views.shop, name='shop'),
       path('about/',views.about, name='about'),
       path('create-recipe/', views.createRecipe, name='create-recipe'),
       path('update-recipe/<str:pk>',views.updateRecipe, name='update-recipe'),
       path('delete-recipe/<str:pk>',views.deleteRecipe, name='delete-recipe')
]
