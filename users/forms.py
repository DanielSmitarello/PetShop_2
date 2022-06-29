from django import forms

class User_profile(forms.Form):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    mail = forms.CharField(max_length = 30)
    pet_name= forms.CharField(max_length = 30)
    profile_img = forms.ImageField(upload_to='profile_image', null = True)