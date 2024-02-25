from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# custom user model
class Account(AbstractUser):
    is_deliveryman = models.BooleanField()
    is_foodie = models.BooleanField()
    is_kitchen = models.BooleanField()