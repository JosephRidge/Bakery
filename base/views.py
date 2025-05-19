from django.shortcuts import render, redirect
from .models import Recipe, Shop
from .forms import RecipeForm, ShopForm


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

"""
We are now starting the CRUD operations by this we mean Create Read Update and Delete
 """
def createRecipe(request):
    form = RecipeForm()  # inialization
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('recipes') 
    context = {'form': form}
    return render(request,'base/recipe_form.html', context)

def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance =recipe)
        form.save()
        return redirect('recipes')

    context = {'form':form}
    return render(request,'base/recipe_form.html', context)

def shop(request):
    return render(request, 'base/shop.html')

# Create operation => POST
def createShop(request):
    form = ShopForm() # instance of the shop form
    if request.method =='POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save() # create the data in DB
            return redirect('shop')
            
    context = {"form":form} 
    return render(request, 'base/shop_form.html', context)


def cart(request):
    return render(request, 'base/cart.html')

def about(request):
    return render(request, 'base/about.html')
