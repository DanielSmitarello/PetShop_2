from django import forms
from petshop.models import Productos

class Product_form(forms.ModelForm):
    # name = forms.CharField(max_length=50)
    # description = forms.CharField(max_length=200)
    # price = forms.FloatField()
    # SKU = forms.CharField(max_length=30)
    # is_active = forms.BooleanField()

    class Meta:
        model = Productos
        fields = '__all__'
