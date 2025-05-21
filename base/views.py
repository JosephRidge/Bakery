from django.shortcuts import render, redirect
from .models import Recipe, Shop
from .forms import RecipeForm, ShopForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def logoutUser(request):
    logout(request)
    messages.info(request, "See you soon!")
    return redirect('login')


def loginUser(request):  
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
 
        # validate that the user exists
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "==> user does not exist!!")  
        
        # authenticate the use
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, f"Welcome home {user.username}")
            return redirect('home')
        else:
            messages.error(request, "Wrong credentials!") 


    return render(request, 'base/login.html')


def home(request):
    return render(request, 'base/home.html')

@login_required(login_url='login')
def recipes(request):
    recipes = Recipe.objects.all() # fetched all the recipes
    context = {"recipes":recipes}
    return render(request, 'base/recipes.html', context)

@login_required(login_url='login')
def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk) 
    context = {'recipe':recipe}
    return render(request, 'base/recipe.html',context)

"""
We are now starting the CRUD operations by this we mean Create Read Update and Delete
 """
@login_required(login_url='login')
def createRecipe(request):
    form = RecipeForm()  # inialization
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('recipes') 
    context = {'form': form}
    return render(request,'base/recipe_form.html', context)

@login_required(login_url='login')
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
@login_required(login_url='login')
def shops(request):
    shops = Shop.objects.all()
    context = {"shops":shops}
    return render(request, 'base/shops.html', context)

# Read one from the DB
@login_required(login_url='login')
def shop(request, pk):
    shop = Shop.objects.get(id=pk)
    context = {"shop": shop}
    return render(request, 'base/shop.html', context)

# update target item
@login_required(login_url='login')
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
@login_required(login_url='login')
def deleteShop(request, pk):
    shop = Shop.objects.get(id=pk)
    context ={"shop":shop}
    if request.method == "POST":
        shop.delete()
        return redirect('shops')
    return render(request, 'base/delete_form.html', context)

# Create operation => POST
@login_required(login_url='login')
def createShop(request):
    form = ShopForm() # instance of the shop form
    if request.method =='POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save() # create the data in DB
            return redirect('shops')
            
    context = {"form":form} 
    return render(request, 'base/shop_form.html', context)

@login_required(login_url='login')
def cart(request):
    return render(request, 'base/cart.html')

def about(request):
    return render(request, 'base/about.html')
