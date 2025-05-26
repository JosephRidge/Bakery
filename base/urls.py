from django.urls import path
from . import views

urlpatterns = [
       path('register/',views.registerUser, name='register'),
       path('logout/',views.logoutUser, name='logout'),
       path('login/',views.loginUser, name='login'),
       path('',views.home, name='home'),
       path('recipe/',views.recipe, name='recipe'),
       path('cart/',views.cart, name='cart'),
       path('shop/',views.shop, name='shop'),
       path('about/',views.about, name='about'), 
       path('create-recipe/',views.recipeForm, name='create-recipe'),
       path('create-shop/',views.recipeForm, name='create-shop'),
       path('update-shop/<str:pk>/',views.updateShop, name='update-shop'),
       path('delete-shop/<str:pk>/',views.deleteShop, name='delete-shop'),

       path('forum/',views.forum, name='forum'),
       path('post/<str:pk>/',views.post, name='post'),
       path('create-post/',views.createPost, name='create-post'),

 ]
