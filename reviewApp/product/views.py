from xml.sax.handler import feature_external_ges
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product, Review
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, ListView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages



def home (request):
    featuredProducts = Product.objects.filter(featured=True)
    featuredProducts = featuredProducts[:6]
    return render(request, 'home.html', context={'featuredProducts':featuredProducts})


def about(request):
    return render(request, 'about.html')

@login_required
def contact(request):
    if request.method == 'POST':
        c_form = contactForm(request.POST)
        if c_form.is_valid():
            subject = c_form.cleaned_data['subject']
            emailsubject = "New Contact Form Message"
            from_email = c_form.cleaned_data['fromEmail']
            message = c_form.cleaned_data['message']

            emailmessage = "You have a new message from " + from_email + ". The subject is: " + subject + " and the message is: " + message
            try:
                send_mail(emailsubject, emailmessage, from_email, ['cscottsysarchsreviewapp@gmail.com'] )
                messages.success(request, "Message Successfully Sent!")
            except BadHeaderError:
                
                return HttpResponse('Invalid header found.')
            return redirect('contact')
            
            
    else:
        c_form = contactForm()

    return render(request, 'contact.html',  context={'c_form':c_form,})


def products(request):
    products = Product.objects.all().order_by('category')
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
