from django.db import models
from .models import Drug


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    user_email = models.EmailField(unique=True) 
    password = models.IntegerField()
    amka = models.IntegerField()
    address = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    tk = models.IntegerField()
    phone = models.IntegerField() 
    
    
    def __str__(self):
        return self.first_name
    
   
class SaleMen(models.Model):
    fname = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    sm_email = models.EmailField(unique=True)
    sm_pass = models.IntegerField()
    sm_storename = models.CharField(max_length=80) 
    sm_address = models.CharField(max_length=70) 
    sm_location = models.CharField(max_length=70) 
    sm_city = models.CharField(max_length=70) 
    sm_tk = models.IntegerField()
    sm_phone= models.IntegerField() 
    sm_afm = models.IntegerField() 
    
    
class Pharmasist(models.Model):
    f_name = models.CharField(max_length=70)
    l_name = models.CharField(max_length=70)
    p_email = models.EmailField(unique=True)
    p_pass = models.IntegerField()
    p_afm = models.IntegerField()
    p_storename = models.CharField(max_length=80) 
    P_address = models.CharField(max_length=70) 
    p_location = models.CharField(max_length=70)
    p_city = models.CharField(max_length=70)
    p_tk = models.IntegerField()
    p_phone = models.IntegerField() 
    sm_id = models.ForeignKey(SaleMen, on_delete=models.CASCADE)
    drug_id = models.ManyToManyField(Drug) 
    