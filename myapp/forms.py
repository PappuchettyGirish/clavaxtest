from django import forms
from django.forms import CharField, Form, PasswordInput
from myapp.models import Userdata
from django.contrib import auth
from django.db.models import Q


class UserForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    username =forms.CharField(label='Username', max_length=50)
    email=forms.EmailField(label='Email')
    password=forms.CharField(label="Password",widget=PasswordInput())
    address=forms.CharField(widget=forms.Textarea) 
    image=forms.ImageField() 
    MIN_LENGTH = 8
    def clean(self):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        cleaned_data = super(UserForm, self).clean()
        password=cleaned_data.get('password')
        if len(password) < self.MIN_LENGTH:
    	    raise forms.ValidationError("The password must be at least %d characters long." % self.MIN_LENGTH)
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("The password must contain at least one digit")
        if not any(char.isupper() for char in password):
            raise forms.ValidationError("The password must contain at least one upper letter")
        if not any(char.islower() for char in password):
            raise forms.ValidationError("The password must contain at least one lower letter")
        if not any(char in special_characters for char in password):
            raise forms.ValidationError("The password must contain at least one special character")
        username=cleaned_data.get('username')
        dbuser=Userdata.objects.filter(name=username)
        if (dbuser):
            raise forms.ValidationError("Username already exists in site. Please try with other.")

class LoginForm(forms.Form):
    username=forms.CharField(label='Username', max_length=50)
    password=forms.CharField(label="Password",widget=PasswordInput())
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username=cleaned_data.get('username')
        password=cleaned_data.get('password')
        dbuser=Userdata.objects.filter(Q(name=username),Q(password=password))
        if not (dbuser):
            raise forms.ValidationError("Username or Password are wrong, Try again")
