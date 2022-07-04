from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}



class Profile_form(forms.Form):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    mail = forms.CharField(max_length = 30)
    pet_name= forms.CharField(max_length = 30)
    #profile_img = forms.ImageField()