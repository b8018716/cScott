from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return HttpResponse('<h1>TEST</h1>')


def about(request):
    return HttpResponse('<h1>about</h1>')

def contact(request):
    return HttpResponse('<h1>contact</h1>')

def products(request):
    return HttpResponse('<h1>products</h1>')

# Create your views here.
