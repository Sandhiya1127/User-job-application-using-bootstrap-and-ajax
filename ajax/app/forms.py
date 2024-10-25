# forms.py
from django import forms
from .models import UserApplication


class UserApplicationForm(forms.ModelForm):
    class Meta:
        model = UserApplication
        fields = ['name', 'email', 'experience', 'job_role', 'resume']

from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password']

