from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Create any username'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Create any password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Write username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Write password'}))

    class Meta:
        model = User
        fields = ['username', 'password']
