from django.shortcuts import render


"""
Render our templates using views
 - View will handle the logic ( request) to what will be rendered
"""
# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def recipe(request):
    return render(request, 'base/recipe.html')

def shop(request):
    return render(request, 'base/shop.html')

def cart(request):
    return render(request, 'base/cart.html')

def about(request):
    return render(request, 'base/about.html')
