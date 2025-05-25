from django.shortcuts import render, redirect
from .models import Recipe, Shop, Author, Post, Comment
from .forms import RecipeForm, ShopForm, PostForm, AuthorForm, CommentForm
from django.contrib import messages

# authentication 
from django.contrib.auth.models import User 
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
 


def forgotPassword(request):
    context = {"form":"n/a"}
    if request.method == "POST":
        username = request.POST.get('username')
        
        try:
            user = User.objects.get(username=username)
            userId = user.id
            print(f"====>> {userId}")
            return redirect('update-password',pk=userId)
        except:
            messages.error(request, "User does not exist!")
        
        
    return render(request, 'base/auth/forgot_pass.html' , context)

def updatePassword(request, pk):
    print(f"====>> ARRIVED! ")
    # user = User.objects.get(id=pk)
    if request.method == "POST":
        password = request.POST.get('password')

    # print(f"====>> {user}")

    return render(request, 'base/auth/pass_change.html')

def registerUser(request):
    form = UserCreationForm()
    authorForm = AuthorForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        authorForm = AuthorForm(request.POST)
        if form.is_valid() and authorForm.is_valid():
            user  = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            bio = authorForm.cleaned_data['bio']
            author = Author.objects.create(
                user = user,
                bio = bio
            )

           # we can choose to login the user or take them to th elogin page let us make their work easier and login them
            user = authenticate( request, username = username, password = password )
            if user is not None: 
                login(request, user)
                messages.info(request, f"Welcome to the family {form.cleaned_data['username']}")                
                return redirect('home')
            else:
                messages.info(request, "wrong credentials ")
        else:
            messages.error(request, "ooops! something went wrong!")
            print(form.error)
    context = {"form":form,"bio":authorForm}
    return render(request, 'base/auth/register.html', context  )


def loginUser(request):
    if request.method == "POST":
        # get user inputs 
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user exists
        try:
            user = User.objects.filter(username = username)
        except:
            messages.error(request, "User does not exixt!")
        
        # validate the user 
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, f"Welcome back {user.username}")
            return redirect('home')
        else:
            messages.error(request, "Wrong credentials!")

    return render(request, 'base/auth/login.html'  )

def logoutUser(request): 
    if request.method =="POST":
        messages.info(request, f"See you soon {request.user.username}")
        logout(request)
        return redirect('login')
    return render(request,'base/auth/logout.html'  )












def home(request):
    return render(request, 'base/home.html')

def createPost(request):
    author = request.user.author
    print(f"==>>>> {author}")
    form = PostForm() 

    if request.method == 'POST':
        form = PostForm(request.POST )  
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']        
            post = Post.objects.create(
            author = author, 
            content= content,
            title = title
              )
            return redirect('forum')
        else:
            print('==> invalid')
    

    context = {"form":form}
    return render(request, 'base/post_form.html', context)

def forum(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, 'base/forum.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk) 
  
    form = CommentForm()
    comments = post.comment_set.all()
    participants = post.participants.all()
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment'] 
            Comment.objects.create(
                comment = comment, 
                author = request.user.author,
                post = post
            )
            participants = post.participants.add(request.user)
            # form.save()
            return redirect('post',pk=pk)
    context = {"post":post,"comments":comments, "form":form,"participants":participants}
    return render(request, 'base/post.html', context)


def comment(request):
    return render(request)

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
    context = {'form': form}
    return render(request,'base/recipe_form.html', context)

@login_required(login_url="login")
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
