from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.db import models
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'username', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password',
            'id': 'hi',
        }
))
class SetUpForm(forms.ModelForm):
        compname=forms.CharField(label="Company Name",max_length=30,widget=forms.TextInput(attrs={'placeholder':'Your Company Name'}))
        phone=forms.CharField(label="Company Phone Number",max_length=30,widget=forms.TextInput(attrs={'placeholder':'Your Company Phone Number'}))
        class Meta:
            model=SetUp
            widgets = {'user': forms.HiddenInput()} 
            exclude=('updated','created')
 
class PlanForm(forms.ModelForm):
    Sunday=Monday=Wednesday=Thursday=Friday=Saturday=forms.BooleanField(required=False)
    v=[i for i in range(1940,2030)]
    date=forms.DateField(label="Choose date",widget=forms.SelectDateWidget(years=v))
    name=forms.CharField(label="Product name",max_length=100,widget=forms.TextInput(attrs={'placeholder':'Enter your company name'}))
    desc=forms.CharField(label="Product Description",max_length=300,widget=forms.TextInput(attrs={'placeholder':'Your Product description'}))
    location=forms.CharField(label="Advert Location",max_length=300,widget=forms.TextInput(attrs={'placeholder':'Location to display advert'}))
    
    class Meta:
        model=AddPlan
        widgets = {'user': forms.HiddenInput()} 
        exclude=('updated','created')
        
class ContactForm(forms.ModelForm):
    name=forms.CharField(label="Full Name",max_length=30,widget=forms.TextInput(attrs={'placeholder':'Name'}))
    email=forms.CharField(label="Email",max_length=30,widget=forms.TextInput(attrs={'placeholder':'Email'}))
    info=forms.CharField(label="Email",max_length=30,widget=forms.TextInput(attrs={'placeholder':'Message'}))
    class Meta:
        model=Contact
        exclude=('updated','created')

class RegistrationForm(UserCreationForm):
    first_name=forms.CharField(label='First Name',max_length=200,required=True,widget=forms.TextInput(attrs={'placeholder':'Firstname'}))
    last_name=forms.CharField(label='Last Name',max_length=200,required=True,widget=forms.TextInput(attrs={'placeholder':'Lastname'}))
    email=forms.EmailField(label='Email',max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username=forms.CharField(label='Username',max_length=200,required=True,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1=forms.CharField(label='Password',required=True,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(label='Confirm Password',required=True,widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model=User
        widgets = {'user': forms.HiddenInput()} 
        fields=('email','username','first_name','last_name','password1','password2')
        
class ItemForm(forms.ModelForm):
    itemname=forms.CharField(label="Company Name",max_length=30,widget=forms.TextInput(attrs={'placeholder':'Your Company Name'}))
    class Meta:
        model=Items
        widgets = {'user': forms.HiddenInput()} 
        fields="__all__"