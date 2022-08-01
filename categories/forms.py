from django.forms import forms 
from .models import Category

class NewCateg(forms.Form):
    categ_name = forms.CharField(max_length=70, required=True) 