from django import forms
from .models import CarBuyer
from django.core.exceptions import ValidationError


class CarBuyerForm(forms.ModelForm):
    class Meta:
        model = CarBuyer
        fields = '__all__'

    
