from django.urls import path
from . import views

urlpatterns = [
       path('register/',views.createUser, name='register'), 
       path('logout/',views.logoutUser, name='logout'), 
       path('login/',views.loginUser, name='login'), 
       path('',views.home, name='home'), 
       path('recipes/',views.recipes, name='recipes'), 
       path('recipe/<str:pk>/',views.recipe, name='recipe'),    
       path('create-recipe/',views.createRecipe, name='create-recipe'),
       path('update-recipe/<str:pk>/',views.updateRecipe, name='update-recipe'),
       path('cart/',views.cart, name='cart'),
       path('my-shop/',views.shops, name='shops'),
       path('my-shop/<str:pk>/',views.shop, name='shop'),
       path('shop/create-shop/',views.createShop, name='create-shop'),
       path('shop/update-shop/<str:pk>/',views.updateShop, name='update-shop'),
       path('shop/delete-shop/<str:pk>/',views.deleteShop, name='delete-shop'),
       path('about/',views.about, name='about'),
       path('forum/',views.forum, name='forum'),
       path('create-post/',views.createPost, name='create-post'),
       path('read-post/<str:pk>/',views.readPost, name='read-post'),
]
