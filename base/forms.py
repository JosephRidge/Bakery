from django.forms import ModelForm 
from .models import Recipe, Shop, Author

class AuthorForm(ModelForm):
    class Meta: # metadata or rather extra information..
        model = Author
        fields =['bio']

class RecipeForm(ModelForm):
    class Meta:  
        model = Recipe
        fields = '__all__'


class ShopForm(ModelForm):
    class Meta: # metadata or rather extra information..
        model = Shop
        fields ='__all__'

