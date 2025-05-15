# Django 101 

## Architecture:

![alt text](image.png)



Forms: 

-> create form.html (u add th submit button state the method, add crsf token)
-> create form.py here we import the modelform from django.forms ( meta class, that has the model and the fields = '__all__')
-> the route to create the form ( urls, view function)
-> test

recall: 
- Create ( input forms )
- Read (read all and read one)
- update ( read the pass it as an instance i.e ModelForm(instance = model,  ))
- Delete ( we create a form and ask if they really want to delete it..)