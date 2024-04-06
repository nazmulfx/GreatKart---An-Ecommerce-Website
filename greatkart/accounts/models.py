from django.db import models

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
# class Accounts(AbstractBaseUser):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_lenght=200)
#     username = models.CharField(max_lenght=200, unique=True)
#     email = models.EmailField(max_length=200, unique=True)
#     phone = models.CharField(max_length=50)
    
#     #Required
#     date_join = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_stuff = models.BooleanField(default=False)
#     is_superadmin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
    
#     USERNAME_FIELD = 'email'