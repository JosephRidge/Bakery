from django.forms import ModelForm
from .models import Recipe, Shop, Author, Comment, Post

class AuthorForm(ModelForm):
    class Meta: 
        model = Author
        fields = ['bio']

class CommentForm(ModelForm):
    class Meta: 
        model = Comment
        fields = ['comment']

class PostForm(ModelForm):
    class Meta: 
        model = Post
        fields = ['title','content']

class RecipeForm(ModelForm):
    class Meta: 
        model = Recipe
        fields = '__all__'

class ShopForm(ModelForm):
    class Meta: 
        model = Shop
        fields = '__all__'
        