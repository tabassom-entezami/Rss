from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(unique=True, blank=False, null=False)
    date_updated = models.DateTimeField(auto_now=True)
    bio = models.TextField(blank=True, null=True)




