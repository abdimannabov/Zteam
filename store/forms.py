from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Your username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"Your password"
    }))

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"Enter password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"Repeat password"
    }))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Username"
            }),
            "email":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"E-Mail"
            })
        }