from django.forms import ModelForm 
from .models import Recipe, Shop , Author, Comment, Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields =['title','content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control item"}) 
        self.fields["content"].widget.attrs.update({"class": "form-control item"}) 

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["decription"].widget.attrs.update({"class": "form-control item h-50"}) 
        self.fields["name"].widget.attrs.update({"class": "form-control item"}) 
        self.fields["prepTime"].widget.attrs.update({"class": "form-control item"}) 
        self.fields["cookTime"].widget.attrs.update({"class": "form-control item"}) 
        self.fields["level"].widget.attrs.update({"class": "form-control item"}) 
        self.fields["ingredients"].widget.attrs.update({"class": "form-control item h-50"}) 
        self.fields["steps"].widget.attrs.update({"class": "form-control item  h-50"}) 
        self.fields["price"].widget.attrs.update({"class": "form-control item"})  


class ShopForm(ModelForm):
    class Meta: # metadata or rather extra information..
        model = Shop
        fields ='__all__'

