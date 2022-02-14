from unicodedata import category
from django.db import models


class Product(models.Model):
    productid = models.AutoField(primary_key=True, )
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    averagecost = models.DecimalField(decimal_places=2, max_digits=8)
    category = models.CharField(max_length=100)
    datereleased = models.DateField()
    description = models.TextField(blank=True)
    productphoto = models.ImageField()

def __str__(self):
    return self.name

# Create your models here.
