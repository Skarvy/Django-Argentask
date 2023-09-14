
from django import forms
from . models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password', 'first_name', 'last_name', 'email']

class LoginForm(forms.Form):
    email = forms.CharField(max_length=150)
    password = forms.CharField(max_length=200)

