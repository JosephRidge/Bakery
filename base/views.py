from django.shortcuts import render, redirect
from .models import Recipe, Shop , Author, Comment, Post
from .forms import RecipeForm, ShopForm, PostForm,AuthorForm, CommentForm
from django.contrib import messages

# authentication 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# MPESA

from django_daraja.mpesa.core import MpesaClient

def createUser(request):
    form = UserCreationForm()  
    bio  = AuthorForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        bio  = AuthorForm(request.POST)

        if form.is_valid() and bio.is_valid():
            user = form.save()
            authorBio = bio.cleaned_data['bio']

            Author.objects.create(
                user = user,
                bio = authorBio
            )

            messages.info(request, "Welcome home!")

            return redirect('login')
        else:
            messages.error(request, "Something went wrong!")

    context = {"form":form, "bio":bio} 
    return render(request, 'base/register.html', context)

def loginUser(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # checked wheyther the user exists in the DB => Users table
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "User does not exist!")
        # authenticated the user and checked whether the credentials are ok
        user = authenticate(request, username=username, password=password) 
        if user is not None: 
            login(request, user)
            messages.error(request, f"Welcome home {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Wrong Credentials")
        
    return render(request, "base/login.html")

def logoutUser(request):
    if request.method == "POST":
        logout(request)
        messages.info(request, "See you soon!")
        return redirect('login')
    return render(request, "base/logout_form.html")

def home(request):
    recipes = Recipe.objects.all()
    context = {"recipes":len(recipes)}
    # cl = MpesaClient()
    # # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    # phone_number = ''
    # amount = 1
    # account_reference = 'reference'
    # transaction_desc = 'Description'
    # callback_url = 'https://api.darajambili.com/express-payment'
    # response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    # print(f"==> {response}")
    return render(request, 'base/home.html', context)

def createPost(request):
    form = PostForm()
    author = request.user.author 

    if request.method == "POST": 
        form = PostForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            Post.objects.create(
                author = author,
                title = title,
                content = content
            )
            return redirect('forum')

    context ={"form":form}
    return render(request, 'base/post_form.html', context)

def forum(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, 'base/forum.html', context)

def readPost(request, pk):
    post = Post.objects.get(id=pk)
    comments =  post.comment_set.all() 
    userContribs = post.contributors.all()
    print(f"====> {userContribs}")
    form = CommentForm()
    author = request.user.author

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            Comment.objects.create(
                post = post,
                author = author, 
                comment = comment
            )
            post.contributors.add(request.user)
            return redirect('read-post',pk=pk)

    context = {"post":post, "form":form, "comments":comments,"contributors":userContribs}
    return render(request, 'base/post.html', context)

def recipes(request):
    recipes = Recipe.objects.all() # fetched all the recipes
    context = {"recipes":recipes}
    return render(request, 'base/recipes.html', context)

@login_required(login_url="login")
def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk) 
    context = {'recipe':recipe}
    return render(request, 'base/recipe.html',context)



"""
We are now starting the CRUD operations by this we mean Create Read Update and Delete
 """
@login_required(login_url="login")
def createRecipe(request):
    form = RecipeForm()  # inialization
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('recipes') 
    context = {'form': form,"from":"create"}
    return render(request,'base/recipe_form.html', context)

@login_required(login_url="login")
def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance =recipe)
        form.save()
        return redirect('recipes')

    context = {'form': form,"from":"update"}
    return render(request,'base/recipe_form.html', context)


def buyRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    context = { "recipe":recipe}
    if request.method == "POST": 
        phoneNumber = request.POST.get('phone')
        cl = MpesaClient() 
        phone_number = phoneNumber
        amount = 1 #int(recipe.price)
        account_reference = 'reference'
        transaction_desc = 'Description'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        # return HttpResponse(response)
        print(f"==> res: {response}")
        messages.info(request, f"STATUS: {response}")

    return render(request, 'base/payment_form.html', context)


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

@login_required(login_url="login")
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

@login_required(login_url="login")
def deleteShop(request, pk):
    shop = Shop.objects.get(id=pk)
    context ={"shop":shop}
    if request.method == "POST":
        shop.delete()
        return redirect('shops')
    return render(request, 'base/delete_form.html', context)

# Create operation => POST

@login_required(login_url="login")
def createShop(request):
    form = ShopForm() # instance of the shop form
    if request.method =='POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save() # create the data in DB
            return redirect('shops')
            
    context = {"form":form} 
    return render(request, 'base/shop_form.html', context)

@login_required(login_url="login")
def cart(request):
    return render(request, 'base/cart.html')

def about(request):
    return render(request, 'base/about.html')
