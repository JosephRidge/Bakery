from django.shortcuts import render, redirect
from .models import Recipe, Shop
from .forms import RecipeForm, ShopForm
from django.contrib.auth.models import User

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username, password)
        print(f"user ==> {user }")

    return render(request, 'base/login.html')


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

# read all from the DB
def shops(request):
    shops = Shop.objects.all()
    context = {"shops":shops}
    return render(request, 'base/shops.html', context)

# Read one from the DB
def shop(request, pk):
    shop = Shop.objects.get(id=pk)
    context = {"shop": shop}
    return render(request, 'base/shop.html', context)

# update target item
def updateShop(request, pk):
    shop = Shop.objects.get(id=pk)
    form = ShopForm(instance= shop)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance = shop)
        form.save()
        return redirect('shops')
    context = {"form":form}
    return render(request, 'base/shop_form.html', context)

# Delete item
def deleteShop(request, pk):
    shop = Shop.objects.get(id=pk)
    context ={"shop":shop}
    if request.method == "POST":
        shop.delete()
        return redirect('shops')
    return render(request, 'base/delete_form.html', context)

# Create operation => POST
def createShop(request):
    form = ShopForm() # instance of the shop form
    if request.method =='POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save() # create the data in DB
            return redirect('shops')
            
    context = {"form":form} 
    return render(request, 'base/shop_form.html', context)


def cart(request):
    return render(request, 'base/cart.html')

def about(request):
    return render(request, 'base/about.html')
