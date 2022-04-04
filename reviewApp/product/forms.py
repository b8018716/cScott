from dataclasses import field, fields
from django import forms
from .models import *


class addReview(forms.ModelForm):

    productRating = forms.IntegerField(label='Product Rating 1-5',min_value=1, max_value=5)

    class Meta:
        model = Review
        fields = ['productRating','reviewContent']