from django.db import models

# Create your models here.
class Product(models.Model):

    title       = models.CharField(max_length= 20)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=3, max_digits=3)    
    summary     = models.TextField()
    featured    = models.BooleanField(default = False)
