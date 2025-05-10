from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class User(AbstractBaseUser):
    avatar= models.TextField(default='/media/avatars/default-avatar.png')
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    last_access = models.DateTimeField(auto_now_add=True)
    
