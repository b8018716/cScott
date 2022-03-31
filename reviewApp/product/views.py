from itertools import product
from webbrowser import get
from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product, Review


def home (request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', context={'products':products})


def productdetail(request, product_id):
    product = Product.objects.get(productid=product_id)
    reviews = Review.objects.filter(product_id=product_id)
    return render(request, 'productdetail.html', context={'product':product, 'reviews':reviews})

def reviews(request):
    return render(request, 'reveiws.html')
# Create your views here.
