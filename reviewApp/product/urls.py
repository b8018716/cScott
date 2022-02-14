from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.products, name='products'),
    path('reviews/', views.reviews, name='reviews')
]
