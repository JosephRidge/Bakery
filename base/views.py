from django.shortcuts import render, redirect
from .forms import RecipeForm, ShopForm


"""
Render our templates using views
 - View will handle the logic ( request) to what will be rendered
"""
from .models import Recipe, Shop

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

def recipeForm(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe')
 
    context = {"form": form}
    return render(request, 'base/recipe_form.html', context)

def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance = recipe)
    if request == 'POST':
        form = RecipeForm(request.POST, instance = recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe')
    contecxt = {'form':form}
    return render(request, 'base/recipe.html',context)

def shop(request):
    shops = Shop.objects.all()
    context = {"shops":shops}
    return render(request, 'base/shop.html', context)

def shopForm(request):
    form = ShopForm()
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop')
    context = {'form':form}
    print(context)
    return render(request, 'base/shop_form.html', context)

def updateShop(request,pk):
    shop = Shop.objects.get(id=pk)
    form = ShopForm(instance=shop)
    if request.method == 'POST':
        form = ShopForm(request.POST,instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop')

    context ={'form':form}
    return render(request, 'base/shop_form.html', context)

def deleteShop(request, pk):
    shop = Shop.objects.get(id=pk)
    if request.method == 'POST':
        shop.delete()
        return redirect('shop')
    return render(request, 'base/delete_item.html',{'obj':shop})


def cart(request):
    return render(request, 'base/cart.html')

def about(request):
    return render(request, 'base/about.html')
 