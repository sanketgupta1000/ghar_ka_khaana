from django.core.validators import RegexValidator
from django.db import models
from user.models import Account

# Create your models here.
class Foodie(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[RegexValidator(regex=r'^\d{10}$', message="Phone number must be of 10 digits.")], max_length=10, help_text='Enter phone number')


class Address(models.Model):
    user = models.ForeignKey(Foodie, on_delete=models.CASCADE)
    residence_id = models.CharField(max_length=30, help_text="Enter a name or number of your residence")
    residency = models.CharField(max_length=30, help_text="Enter your society or apartment name")
    street = models.CharField(max_length=30, help_text="Enter your street name")
    area = models.CharField(max_length=30, help_text="Enter your area of city")
    pincode = models.CharField(max_length=6, validators=[RegexValidator(regex=r"^\d{6}$", message="Pincode must be of 6 digits")], help_text="Enter your postal code")




