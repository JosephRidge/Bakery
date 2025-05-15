from django.shortcuts import render


"""
Render our templates using views
 - View will handle the logic ( request) to what will be rendered
"""
from .models import Recipe

def home(request):
    return render(request, 'base/home.html')

def recipe(request):
    recipes = Recipe.objects.all() # fetched all the recipes
    context = {"recipes":recipes}
    return render(request, 'base/recipe.html', context)

def reciperForm(request):

    return render(request, 'base/recipe_form.html')

def shop(request):
    return render(request, 'base/shop.html')

def cart(request):
    return render(request, 'base/cart.html')

def about(request):
    return render(request, 'base/about.html')
