from django.forms import ModelForm
from .models import Recipe, Shop

class RecipeForm(ModelForm):
    class Meta: 
        model = Recipe
        fields = '__all__'

class ShopForm(ModelForm):
    class Meta: 
        model = Shop
        fields = '__all__'
        