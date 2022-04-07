from django import forms
from .models import *



class CarSaleForm(forms.ModelForm):

    class Meta:
        model = CarSaler
        # fields = ['seller_name', 'seller_mobile', 'email', 'make', 'model','year', 'Condition', 'asking_price', 'picture']
        exclude = ('is_sell',)

    def clean_password(self):
        price = self.cleaned_data['asking_price']
        if len(price) < 1000 and len(price) > 100000:
            raise forms.ValidationError("password is too short")
        return price
