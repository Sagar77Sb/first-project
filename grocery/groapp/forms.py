from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(forms.ModelForm):
    class Meta:
        model= Registration
        fields=['user','name','mobile_no','city']


class LoginForm(forms.Form):
    username=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(max_length=10,widget=forms.PasswordInput(attrs={'class':'form-control'}))