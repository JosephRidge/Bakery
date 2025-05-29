from rest_framework.serializers import ModelSerializer
from base.models import Recipe, Author, Post, Shop

class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class RecipeSerializer(ModelSerializer):
    class Meta: 
        model = Recipe
        fields = '__all__'



