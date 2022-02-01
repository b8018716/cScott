from itertools import product
from django.contrib import admin
from .models import Product

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','brand']

# Register your models here.
