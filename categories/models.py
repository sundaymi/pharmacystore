from django.db import models

# Create your models here.

class Category(models.Model):
    c_name = models.CharField(max_length=80)
    
    def __str__(self):
        return self.c_name
    
    
class Manufacturer(models.Model):
    man_name = models.CharField(max_length=80)
    
    def __str__(self):
        return self.man_name 
    
    