from ast import Return
from cmath import rect
from itertools import product
from multiprocessing import context
from pyexpat import model
from re import template
import re
from sre_constants import SUCCESS
from typing import List
from .forms import *
from webbrowser import get
from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product, Review
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, ListView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404



def home (request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', context={'products':products})


def productdetail(request, product_id):
    product = Product.objects.get(productid=product_id)
    reviews = Review.objects.filter(product_id=product_id).order_by('-datePosted')
    print(reviews)
    reviewFour = reviews[:4]
    print(reviewFour)
    new_review = None
    if request.method == 'POST':
        rForm = addReview(data=request.POST, instance=new_review)
        if rForm.is_valid():
            new_review = rForm.save(commit=False)
            new_review.product = product
            new_review.author = request.user
            new_review.save()
            rForm = addReview()
            return HttpResponseRedirect("/products/shop/%s" % product_id) 
    else:
        rForm = addReview()

    
    return render(request, 'productdetail.html', context={'product':product, 'reviews':reviews, 'rForm':rForm, 'new_review':new_review, 'reviewFour':reviewFour})

class ReviewListView(ListView):
    model = Review

    template_name = 'reviewlist.html'
    context_object_name = 'reviews'
    paginate_by = 5
    


    def get_queryset(self):
        self.product = get_object_or_404(Product, productid = self.kwargs['product_id'] )
        
        return Review.objects.filter(product_id=self.product).order_by('-datePosted')

class UserReviewListView(ListView):
    model = Review
    template_name = 'reviewlistuser.html'
    context_object_name = 'reviews'
    paginate_by = 5


    def get_queryset(self):
        self.user = get_object_or_404(User, id = self.kwargs['author_id'])
        print(self.user)
        return Review.objects.filter(author_id=self.user).order_by('-datePosted')

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviewdetail.html'


class ReviewUpdateView(UserPassesTestMixin, UpdateView):
    model = Review
    template_name = 'reviewupdate.html'

    fields= ['productRating','reviewContent']

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
         
            return True
            
        return False
    


    def form_valid(self, form):
        
        form.instance.author = self.request.user
        print("Form is valid")
        return super().form_valid(form)

    
class ReviewDeleteView(UserPassesTestMixin,DeleteView):
    model = Review
    success_url = "/shop"
    template = 'reviewdelete.html'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
         
            return True
            
        return False

# Create your views here.
