from django import forms
from .models import CarBuyer
from django.core.exceptions import ValidationError


class CarBuyerForm(forms.ModelForm):
    class Meta:
        model = CarBuyer
        fields = '__all__'

    def asking_price(self):
        print("check the data")
        data = self.cleaned_data['asking_price']
        print(data, "=-=-=")
        if len(data) < 1000 and len(data) > 100000:
            raise ValidationError(
                "price less than 100000 & greater than 1000!")

        return data
