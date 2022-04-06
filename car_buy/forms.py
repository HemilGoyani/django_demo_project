from tkinter.tix import Form
from django import forms
from .models import CarBuyer


class CarBuyerForm(forms.ModelForm):
    class Meta:
        model = CarBuyer
        fields = '__all__'
