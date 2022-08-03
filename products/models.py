from django.db import models
from categories import Category, Manufacturer
from .models import Pharmasists

# Create your models here.

class Drug(models.Model):
    d_name = models.CharField(max_length=80)
    manufactured_name = models.CharField(max_length=80)
    category_name = models.CharField(max_length=80)
    manufactured_price = models.DecimalField(max_digits=10, decimal_places=10)
    price = models.DecimalField(max_digits=10, decimal_places=10) 
    stock = models.IntegerField()
    date_expiration = models.DateField() 
    categ_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    manuf_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.d_name