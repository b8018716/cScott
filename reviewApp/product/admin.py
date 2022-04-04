from atexit import register
from csv import list_dialects
from itertools import product
from pyexpat import model
from django.contrib import admin
from .models import Product, Review, Phone, Tablet, Laptop

class reviewInLine(admin.TabularInline):
    model = Review
    max_num = 2
    can_delete = False
    readonly_fields = ('author','productRating','reviewContent')



class ProductAdmin(admin.ModelAdmin):
    list_display=['name','brand','category']
    inlines = [reviewInLine]

    


class ReviewAdmin(admin.ModelAdmin):
   list_display=['author','product','productRating','datePosted',]
        
   
class PhoneAdmin(ProductAdmin):
    list_display=['name','brand','averagecost','dimensions','datereleased']

class LaptopAdmin(ProductAdmin):
    list_display=['name','brand','averagecost','operatingsystem','amountOfRam','memorySize','processor','datereleased']

class TabletAdmin(ProductAdmin):
    list_display=['name','brand','averagecost','screensize','datereleased']




admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Tablet, TabletAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Product, ProductAdmin)
