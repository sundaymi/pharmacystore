from django.db import models

# Create your models here.

class Timologio(models.Model):
    t_name = models.CharField(max_length=100)
    manufactured = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=10)
    quantity = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=10)
    