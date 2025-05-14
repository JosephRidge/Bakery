from django.shortcuts import render


"""
Render our templates using views
 - View will handle the logic ( request) to what will be rendered
"""
from .models import Recipe

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

"""
SQL : 
SELECT *  FROM Recipes; 

'
'
ORM
'
'

django:   
recipes = Recipe.object.all() 
"""

def recipe(request):
    recipes = Recipe.objects.all() 
    context = {"recipes": recipes}
    return render(request, 'base/recipe.html', context)

def shop(request):
    return render(request, 'base/shop.html')

def cart(request):
    return render(request, 'base/cart.html')

def about(request):
    return render(request, 'base/about.html')
