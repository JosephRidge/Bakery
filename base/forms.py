from django.forms import ModelForm
from .models import Recipe

class RecipeForm(ModelForm):
    class Meta: # metadata => extra information
        model = Recipe
        fields = '__all__'
