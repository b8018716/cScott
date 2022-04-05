from dataclasses import field, fields
from operator import truediv
from pickle import TRUE
from django import forms
from .models import *


class addReview(forms.ModelForm):

    productRating = forms.IntegerField(label='Product Rating 1-5',min_value=1, max_value=5)

    class Meta:
        model = Review
        fields = ['productRating','reviewContent']

class contactForm(forms.Form):
    fromEmail = forms.EmailField(label='Your Email',required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)