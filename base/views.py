from django.shortcuts import render, redirect


"""
Render our templates using views
 - View will handle the logic ( request) to what will be rendered
"""
from .models import Recipe
from .forms import  RecipeForm

def home(request):
    return render(request, 'base/home.html')

def recipe(request):
    recipes = Recipe.objects.all() # fetched all the recipes
    context = {"recipes":recipes}
    return render(request, 'base/recipe.html', context)

def createRecipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe') 
    context ={"form": form}

    return render(request, 'base/recipe_form.html', context)

def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance = recipe)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe') 
    context ={"form": form}

    return render(request, 'base/recipe_form.html', context)

def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    context = {"recipe": recipe}
    if request.method == "POST":
        recipe.delete()
        return redirect('recipe')
    return render(request , 'base/delete_form.html', context)


def shop(request):
    return render(request, 'base/shop.html')

def cart(request):
    return render(request, 'base/cart.html')

def about(request):
    return render(request, 'base/about.html')
