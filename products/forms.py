from django.forms import forms
from .models import Drug 

class NewProduct(forms.Form):
    n_prod = forms.CharField(max_length = 70) 
    manufactured_name = forms.CharField(max_length=80)
    category_name = forms.CharField(max_length=80)
    manufactured_price = forms.DecimalField(required=True)
    price = forms.DecimalField(required=True)
    stock = forms.IntegerField(required=False)
    date_expiration = forms.DateTimeField(required=True)
    image = forms.ImageField(required=True)
    
    