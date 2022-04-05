from django import forms
from .models import *


class CarSaleForm(forms.ModelForm):
    class Meta:
        model = CarSaler
        # fields = ['seller_name', 'seller_mobile', 'email', 'make', 'model','year', 'Condition', 'asking_price', 'picture']
        exclude = ('is_sell',)
        
