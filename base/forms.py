from django.forms import ModelForm, TextInput
from .models import Recipe

class RecipeForm(ModelForm):
    class Meta: # metadata => extra information
        model = Recipe
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control flex form-control form-control-lg ", 
                }),
        }
