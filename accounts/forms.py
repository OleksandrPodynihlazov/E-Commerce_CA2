from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('username','email','age',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','email','age',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','age',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)