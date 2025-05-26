from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    genderClass = {
        'M':'Male',
        'F':'Female'
    }
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100) 
    gender = models.CharField(max_length=1, choices=genderClass)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
        

    def __str__(self):
        return self.name

# representation of your table in your DB

"""
#SQL 

CREATE TABLE recipe ( 
    name VARCHAR(255),
    description LONGTEXT,  
    prepTime INT,
    cookTime INT, 
    level VARCHAR(100),
    ingredients LONGTEXT,
    steps LONGTEXT 
    );

    CRUD ===> DBs
    SCHEMA=> blueprint of a table-> class
    from the schema we create a table and create records 
"""
class Recipe(models.Model):    
    cookingLevels = { 
        "B": "Beginner",  
        "I": "Intermediate",
        "P":"Pro"
    }
    name = models.CharField(max_length=255) # "Coaching Rugby by Antony"
    decription = models.TextField() #  
    prepTime = models.IntegerField()
    cookTime = models.IntegerField()
    level = models.CharField(max_length=1, choices=cookingLevels) 
    ingredients = models.TextField() 
    steps = models.TextField() 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta: 
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.name
    
class Shop(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True) 
    owner_name = models.CharField(max_length=255) 
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    open_time = models.TimeField()
    close_time = models.TimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['-updated_at','-created_at']

    def __str__(self):
        return self.name


class Author (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Post (models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    participants = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return f"Post by {self.author.user.username}"

class Comment (models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 
    post =  models.ForeignKey(Post, on_delete=models.CASCADE) 
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return f"by {self.author.user.username}"