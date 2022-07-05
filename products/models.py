from django.db import models

# Create your models here.

class Drug(models.Model):
    d_name = models.CharField(max_length=80)
    manufactured_name = models.CharField(max_length=80)
    category_name = models.CharField(max_length=80)
    manufactured_price = models.DecimalField(max_digits=10, decimal_places=10)
    price = models.DecimalField(max_digits=10, decimal_places=10) 
    stock = models.IntegerField()
    date_expiration = models.DateField() 