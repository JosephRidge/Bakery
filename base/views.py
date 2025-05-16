from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm


def home(request):
    return render(request, 'base/home.html')

def recipes(request):
    recipes = Recipe.objects.all() # fetched all the recipes
    context = {"recipes":recipes}
    return render(request, 'base/recipes.html', context)

def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk) 
    context = {'recipe':recipe}
    return render(request, 'base/recipe.html',context)

def createRecipe(request):
    form = RecipeForm()

    if request.method == 'POST':
        if form.is_valid():
            form = RecipeForm(request.POST)
            form.save()
            print(form)
            return redirect('recipes')

    context = {'form': form}
    return render(request,'base/recipe_form.html', context)

def shop(request):
    return render(request, 'base/shop.html')

def cart(request):
    return render(request, 'base/cart.html')

def about(request):
    return render(request, 'base/about.html')
