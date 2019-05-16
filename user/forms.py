from django import forms
from .models import RATING_CHOICES



class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=128, required=True)
    password = forms.CharField(label="Password", max_length=128, required=True, widget=forms.PasswordInput())

