from django import forms
from .models import *


class CarSaleForm(forms.ModelForm):
    class Meta:
        model = CarSaler
        fields = '__all__'
        
