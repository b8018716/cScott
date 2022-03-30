from atexit import register
from itertools import product
from pyexpat import model
from django.contrib import admin
from .models import Product, Review

class reviewInLine(admin.TabularInline):
    model = Review
    max_num = 2
    can_delete = False
    readonly_fields = ('author','productRating','reviewContent')



class ProductAdmin(admin.ModelAdmin):
    list_display=['name','brand',]
    inlines = [reviewInLine]


class ReviewAdmin(admin.ModelAdmin):
   list_display=['author','product','productRating','datePosted',]
   




admin.site.register(Review, ReviewAdmin)
admin.site.register(Product, ProductAdmin)
