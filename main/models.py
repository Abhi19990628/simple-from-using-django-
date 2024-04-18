from django.db import models

# Create your models here.
class person(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    email=models.EmailField()
    phone_number=models.CharField(max_length=10)
    
    