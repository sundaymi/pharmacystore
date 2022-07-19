from tkinter import CASCADE
from django.db import models
from .models import Pharmasists

# Create your models here.

class Timologio_Pharmasist_SaleMen(models.Model):
    t_name = models.CharField(max_length=100)
    manufactured = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=10)
    quantity = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=10)
    date_order = models.DateTimeField()
    p_id = models.ForeignKey(Pharmasists, on_delete=models.CASCADE)
    

class Apodeiksi_Pharmasist_User(models.Model):
    a_name = models.CharField(max_length=100)
    p_id = models.ForeignKey(Pharmasists, on_delete=models.CASCADE)
    d_name = models.ForeignKey()
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=10)
    date_order = models.DateTimeField() 
    