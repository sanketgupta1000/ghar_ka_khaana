from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    is_foodie  = models.BooleanField(default=False)
    is_kitchen  = models.BooleanField(default=False)
    is_deliveryman  = models.BooleanField(default=False)