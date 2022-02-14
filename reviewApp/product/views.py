from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    return render(request, 'products.html')

def reviews(request):
    return render(request, 'reveiws.html')
# Create your views here.
