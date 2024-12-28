from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class NewUser(AbstractUser):
    mobile = models.CharField(max_length=20)
    forget_password_token = models.CharField(max_length=100,null=True)



class Customer(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    lname = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length = 255)
    PhoneNumber = models.CharField(max_length = 13) 
    FromEmailAddress = models.EmailField(max_length = 100) 
    Comments = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True,blank = True)





