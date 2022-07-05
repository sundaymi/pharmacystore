from django.db import models

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
    
    
class Pharmasists(models.Model):
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
    #sales_id = 
    
    
class SaleMen(models.Model):
    fname = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    sm_email = models.EmailField(unique=True)
    sm_pass = models.IntegerField()
    sm_phone= models.IntegerField() 
    afm = models.IntegerField() 
    