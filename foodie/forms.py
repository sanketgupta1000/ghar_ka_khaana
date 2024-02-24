from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Foodie,Address

class FoodieCreationForm(UserCreationForm):
    
    class Meta:
        model = Foodie
        fields = ['username', 'email', 'password1', 'password2', 'phone_number']

class FoodieAuthenticationForm(AuthenticationForm):

    class Meta:
        model = Foodie
        fields = ['username', 'password']

class AddressCreationForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['residence_id', 'residency', 'street', 'area', 'pincode']
