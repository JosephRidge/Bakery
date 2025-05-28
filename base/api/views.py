from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from django.http import JsonResponse



def getRoutes(request):
    routes =[
        'GET /api/recipes',
        'GET /api/posts',
    ]
    return JsonResponse(routes, safe=False) # safe allows it to turn into json response