from django.forms import ModelForm 
from .models import Recipe, Shop , Author, Comment, Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields =['title','content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["content"].widget.attrs.update({"class": "form-control h-75"})

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['bio']


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

