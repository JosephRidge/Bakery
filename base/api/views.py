from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Recipe
from .serializers import RecipeSerializer

def getData(request):
    routes = [
        'GET api/', 
        'GET api/recipes/', 
        'GET api/posts/'
    ]

    return JsonResponse(routes, safe=False)

@api_view(['GET'])
def getRecipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)
