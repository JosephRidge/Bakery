from django.forms import ModelForm 
from .models import Recipe, Shop , Author, Comment, Post, MyUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = MyUser
        fields = '__all__'

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ["email", "password", "date_of_birth", "is_active", "is_admin"]


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

