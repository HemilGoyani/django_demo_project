from django import forms
from .models import *


class CarSaleForm(forms.ModelForm):

    class Meta:
        model = CarSaler
        exclude = ('is_sell',)
        error_messages = {
            'asking_price': {
                'MinMoneyValidator': ("Proce shoul be greater than 1000."),
                'MaxMoneyValidator': ("Proce shoul be less than 100000."),
            },
        }

    # def asking_price(self):
    #     data = self.cleaned_data['asking_price']

    #     if len(data) < 1000 and len(data) > 100000:
    #         raise forms.ValidationError(
    #             "Enter price less than 100000 & greater than 1000")

    #     return data
