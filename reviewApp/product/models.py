from datetime import datetime
from distutils.command.upload import upload
from itertools import product
from sqlite3 import Date
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    productid = models.AutoField(primary_key=True, )
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    averagecost = models.DecimalField(decimal_places=2, max_digits=8)
    category = models.CharField(max_length=100)
    datereleased = models.DateField()
    description = models.TextField(blank=True)
    productphoto = models.ImageField(upload_to='productPhotos', verbose_name='Product')
    
    def __str__(self):
        return self.name



class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    productRating = models.IntegerField(null=True)
    reviewContent = models.TextField(null=True)
    datePosted = models.DateTimeField(auto_now_add=True)
    

    



# Create your models here.
