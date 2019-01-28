from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UsernameField
from django import forms


class MyLoginForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username', 'class': 'form-control', 'required': True}),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'required': True, 'class': 'form-control'}),
    )