from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import CLUserManager

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    gender_mark = models.CharField(max_length=20,null=True,blank=True)
    full_name = models.CharField(max_length=200,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=False,blank=False)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    mobile_number = models.CharField(max_length=20,null=False,blank=False)
    email = models.EmailField(null=False,blank=False,unique=True)
    password = models.CharField(max_length=200,null=False,blank=False)
    age = models.CharField(max_length=20,null=True,blank=True)
    gender = models.CharField(max_length=30,null=True,blank=True)
    

    date = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    objects = CLUserManager()

    REQUIRED_FIELDS = []

    def get_full_name(self):
        print(self.first_name + self.last_name)
        return self.first_name + self.last_name

    def __str__(self):
        return self.email
