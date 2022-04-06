from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    productid = models.AutoField(primary_key=True, )
    name = models.CharField('Name',max_length=100)
    brand = models.CharField('Brand',max_length=100)
    averagecost = models.DecimalField('Price',decimal_places=2, max_digits=8)
    categoryChoices = ('Phone','Phone'),('Tablet','Tablet'),('Laptop','Laptop'),('Miscellaneous','Miscellaneous')
    category = models.CharField(max_length=100, choices=categoryChoices, null=True, default='Miscellaneous')
    datereleased = models.DateField('Date Released')
    description = models.TextField('Description',blank=True)
    productphoto = models.ImageField(upload_to='productPhotos', verbose_name='Product')
    featured = models.BooleanField(default=False, null=True)
    
    class Meta:
        verbose_name= "All Products"
        verbose_name_plural = " All Products"


    def __str__(self):
        return self.name

class Phone(Product):
    numberOfCameras = models.IntegerField('Number Of Cameras',null=True)
    dimensions = models.CharField('Dimensions',max_length=100,null=True)
    screensize = models.CharField('Screen Resolution',max_length=100,null=True)
    operatingsystem = models.CharField('Operating System',max_length=100,null=True)
    memorySize = models.IntegerField('Memory Capacity',null=True)

    class Meta:
        
        verbose_name_plural = " Phones"
    
class Laptop(Product):
    operatingsystem = models.CharField('Operating System',max_length=100,null=True)
    amountOfRam = models.DecimalField('RAM Amount',decimal_places=2, max_digits=8, null=True)
    memorySize = models.IntegerField('Memory Capacity',null=True)
    processor = models.CharField('Processor',max_length=100, null=True)

    class Meta:
        
        verbose_name_plural = " Laptops"



class Tablet(Product):
    screensize = models.CharField('Screen Resolution',max_length=100)
    operatingsystem = models.CharField('Operating System',max_length=100,  null=True)

    class Meta:
        verbose_name_plural = " Tablets"


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    productRating = models.PositiveIntegerField('Rating',null=True,validators=[MaxValueValidator(5)] )
    reviewContent = models.TextField('Content of Review',null=True)
    datePosted = models.DateTimeField('Posted',auto_now_add=True)
    preview = models.TextField(null=True)
    
    class Meta:
        verbose_name_plural = "Reviews"

    def save(self, *args, **kwargs):
        self.preview = self.reviewContent[0:140] + '...' 
       
        super(Review, self).save(*args, *kwargs)
    
    def get_absolute_url(self):
        return reverse('productdetail', kwargs={'product_id':self.product.pk})

    def __str__(self):
        test = self.author.username + 's review of ' +  self.product.name
        return test


# Create your models here.
