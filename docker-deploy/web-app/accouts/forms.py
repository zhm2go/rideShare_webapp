from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MyUser

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=100, required=True, widget=forms.EmailInput())
    #isDriver = forms.BooleanField(initial=False, required=False, widget=forms.HiddenInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
#
# class SignUpForm(UserCreationForm):
#     email = forms.CharField(max_length=100, required=True, widget=forms.EmailInput())
#     class Meta:
#         model = MyUser
#         fields = ('username', 'email', 'password1', 'password2')