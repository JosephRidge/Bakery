from django.shortcuts import render, redirect
from .forms import RecipeForm, ShopForm  
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

"""
Render our templates using views
 - View will handle the logic ( request) to what will be rendered
"""
from .models import Recipe, Shop

# Creat your views here.


def loginUser(request):   
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "No such username!")

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.info(request, f"Welcome home, {user.username}")
            return redirect('home')
        else:
            messages.error(request, "Wrong credentials!")

    return render(request, 'base/auth/login.html')

def logoutUser(request): 
    logout(request)
    return redirect('login')

def registerUser(request):  
    form = UserCreationForm()
    context = {"form":form}

    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('login')
    return render(request, 'base/auth/register.html', context)

def home(request):
    return render(request, 'base/home.html')
 
@login_required(login_url='login')
def recipe(request):
    recipes = Recipe.objects.all() 
    context = {"recipes": recipes}
    return render(request, 'base/recipe.html', context)

@login_required(login_url='login')
def recipeForm(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe') 
    context = {"form": form}
    return render(request, 'base/recipe_form.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def shop(request):
    shops = Shop.objects.all()
    context = {"shops":shops}
    return render(request, 'base/shop.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteShop(request, pk):
    shop = Shop.objects.get(id=pk)
    if request.method == 'POST':
        shop.delete()
        return redirect('shop')
    return render(request, 'base/delete_item.html',{'obj':shop})

@login_required(login_url='login')
def cart(request):
    return render(request, 'base/cart.html')

def about(request):
    return render(request, 'base/about.html')
 