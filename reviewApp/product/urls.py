from pathlib import Path
from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.products, name='products'),
    #path('reviews/', views.reviews, name='reviews'),
    path('shop/<int:product_id>/', views.productdetail, name='productdetail'),
    path('review/<int:pk>/update/', login_required(views.ReviewUpdateView.as_view()), name='reviewupdate'),
    path('reviews/<int:product_id>', login_required(views.ReviewListView.as_view()), name='reviewlist'),
    path('review/<int:pk>', login_required(views.ReviewDetailView.as_view()), name='reviewdetail'),
    path('review/<int:pk>/delete/', login_required(views.ReviewDeleteView.as_view()), name='reviewdelete'),
    path('reviews/user/<int:author_id>', login_required(views.UserReviewListView.as_view()), name='userreviewlist'),
]
