from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=50)
    role = models.CharField(max_length=50)
    password = models.EmailField(max_length=50)
    otp = models.BigIntegerField()
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_created = models.BooleanField(default=True)
    is_updated = models.BooleanField(default=True)

class Employee(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Firstname = models.CharField(max_length = 50)
    Lastname = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 50)
    contact = models.CharField(max_length = 50)

class Hirer(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Firstname = models.CharField(max_length = 50)
    Lastname = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    contact = models.CharField(max_length = 50)