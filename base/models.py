from django.db import models

# Create your models here.

from django.contrib.auth.models import User

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

    # organize from the latest to the oldest
    class Meta:
        ordering =['-updated_at','-created_at']

    def __str__(self):
        return self.name
    

class Shop(models.Model):
    productName = models.CharField(max_length=150) 
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering =['-updated_at','-created_at']

    def __str__(self):
        return self.productName
    
"""
========================================================================
"""

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # one to one relationship
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #one to many relationship
    title = models.CharField(max_length = 100)
    content = models.TextField()
    people = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering =['-updated_at', '-created_at']
    
    def __str__(self):
        return f"Post by {self.author.user.username}"

class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #one to many relationship
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #one to many relationship 
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering =['-updated_at', '-created_at']
    
    def __str__(self):
        return f"by {self.author.user.username}"
