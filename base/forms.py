from django.forms import ModelForm 
from .models import Recipe, Shop , Author, Comment, Post

 
class AuthorForm(ModelForm):
    class Meta:  
        model = Author
        fields = ['bio']
 
class PostForm(ModelForm):
    class Meta:  
        model = Post
        fields = ['title','content']

class CommentForm(ModelForm):
    class Meta:  
        model = Comment
        fields = ['comment']

class RecipeForm(ModelForm):
    class Meta:  
        model = Recipe
        fields = '__all__'


class ShopForm(ModelForm):
    class Meta: # metadata or rather extra information..
        model = Shop
        fields ='__all__'

