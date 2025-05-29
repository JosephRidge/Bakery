
from base.models import Recipe, Author, Post, Shop
from rest_framework.response import Response
from rest_framework.decorators import   api_view
from .serializers import RecipeSerializer, ShopSerializer, PostSerializer


@api_view(['GET'])
def getShops(request):
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPost(request, id):
    posts = Post.objects.get(id=id)
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)

















@api_view(['GET'])
def getRecipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes,many=True )
    return Response(serializer.data)