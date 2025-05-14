from django.db import models

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

    def __str__(self):
        return self.name
    


