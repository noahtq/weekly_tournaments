from enum import unique
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    # phone_number_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$')
    # phone_number = forms.CharField(validators=[phone_number_regex], max_length=16, unique=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']