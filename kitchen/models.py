from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, RegexValidator
from user.models import Account


# Create your models here.

# model to represent a kitchen
class Kitchen(Account):

    # status of kitchen: online or offline
    status = models.CharField(max_length=50, default="off", choices=[("on","online"), ("off","offline")])

    # address of kitchen
    residence_id = models.CharField(max_length=30, help_text="Enter a name or number of your residence")
    residency = models.CharField(max_length=30, help_text="Enter your society or apartment name")
    street = models.CharField(max_length=30, help_text="Enter your street name")
    area = models.CharField(max_length=30, help_text="Enter your area of city")
    pincode = models.CharField(max_length=6, validators=[RegexValidator(regex=r"^\d{6}$", message="Pincode must be of 6 digits")], help_text="Enter your postal code")


# model defination of "Tiffin"
class Tiffin(models.Model):

    # foreign key of kitchen to determine 'By whom this tiffin is done'
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    
    # price of 1 tiffin
    price = models.IntegerField()

    # date of availibiity 
    date = models.DateField()

    # end time for taking order
    end_time = models.TimeField()

    # maximum quantity available
    max_quantity_available = models.PositiveIntegerField()


# model to represent a tiffin item category, like Bread, Sabji, Dessert
class TiffinItemCategory(models.Model):

    # name of the category
    name = models.CharField(max_length=100)

    # description of the category
    description = models.TextField()


# models to represent an item in a tiffin, like thepla, aloo-matar, etc
class TiffinItem(models.Model):

    # category of the item
    category = models.ForeignKey(TiffinItemCategory, on_delete=models.CASCADE)

    # which tiffin this item belongs to
    tiffin = models.ForeignKey(Tiffin, on_delete=models.CASCADE)

    # name of the item
    name = models.CharField(max_length = 150)

    # qty in one tiffin
    qty_per_tiffin = models.IntegerField(validators=[MinValueValidator(1)])