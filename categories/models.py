from django.db import models

# Create your models here.

class Category(models.Model):
    c_name = models.CharField(max_length=80)
    
    
class Manufacturer(models.Model):
    man_name = models.CharField(max_length=80)