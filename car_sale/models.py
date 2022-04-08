from django.db import models

# Create your models here.

from django.db import models
from django.core.validators import *
from datetime import datetime
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator


class CarSaler(models.Model):
    POOR = 'Poor'
    FAIR = 'Fair'
    GOOD = 'Good'
    EXCELLENT = 'Eexcellent'
    CHOICES = (
        (POOR, "poor"),
        (FAIR, "fair"),
        (GOOD, "good"),
        (EXCELLENT, 'excellent'),
    )
    year_dropdown = []
    for y in range(2011, (datetime.now().year + 1)):
        year_dropdown.append((y, y))
    saler_name = models.CharField(max_length=20)
    saler_mobile = models.CharField(max_length=10, validators=[
                                    MinLengthValidator(10), MaxLengthValidator(10)])
    email = models.EmailField(null=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField(
        ('year'), choices=year_dropdown, default=datetime.now().year)
    condition = models.CharField(max_length=10, choices=CHOICES)
    asking_price = MoneyField(max_digits=8,
                              decimal_places=2, validators=[
                                  MinMoneyValidator(Money(1000, 'USD')),
                                  MaxMoneyValidator(Money(100000, 'USD')),
                              ], default_currency='USD', error_messages={
                                  "message": "price should be less than 100000 & greater than 1000."
                              })
    is_sell = models.BooleanField(default=False)

    def __str__(self):
        return self.saler_name
