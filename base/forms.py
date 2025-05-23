from django.forms import ModelForm 
from .models import Recipe, Shop, Post, Comment, Author

class RecipeForm(ModelForm):
    class Meta:  
        model = Recipe
        fields = '__all__'


class ShopForm(ModelForm):
    class Meta: # metadata or rather extra information..
        model = Shop
        fields ='__all__'

class PostForm(ModelForm):
    class Meta: # metadata or rather extra information..
        model = Post
        fields ='__all__'


class CommentForm(ModelForm):
    class Meta: # metadata or rather extra information..
        model = Comment
        fields =['comment']


class AuthorForm(ModelForm):
    class Meta: # metadata or rather extra information..
        model = Author
        fields =['bio']

        