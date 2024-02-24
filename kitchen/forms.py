from django.contrib.auth.forms import UserCreationForm
from .models import Kitchen
from django import forms

# form to help kitchen in creating account
class KitchenCreationForm(UserCreationForm):

    class Meta:
        model = Kitchen
        fields = ("username", "first_name", "last_name", "email", "residence_id", "residency", "street", "area", "pincode", "password1", "password2")

# will use AuthenticationForm for login