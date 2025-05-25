from django.forms import ModelForm 
from .models import Recipe, Shop, Author, Post, Comment

class AuthorForm(ModelForm):
    class Meta: # metadata or rather extra information..
        model = Author
        fields =['bio']

class PostForm(ModelForm):
    class Meta:  
        model = Post
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta:  
        model = Comment
        fields = '__all__'

class RecipeForm(ModelForm):
    class Meta:  
        model = Recipe
        fields = '__all__'


class ShopForm(ModelForm):
    class Meta: # metadata or rather extra information..
        model = Shop
        fields ='__all__'

