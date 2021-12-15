from django.db import models
from django.contrib.auth.models import AbstractUser

#abstractuser insted of abstractbase user because here only adding to exting auth model

# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)

    

