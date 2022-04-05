from django.db import models
from django.core.validators import *
from datetime import datetime


class CarBuyer(models.Model):
    
    buyer_name = models.CharField(max_length=20)
    buyer_mobile = models.CharField(max_length=10, validators=[
                                    MinLengthValidator(10), MaxLengthValidator(10)])
    make = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, null=True)
    year = models.IntegerField(default=2022)
    Condition = models.CharField(max_length=10, default='Good')
    asking_pricce = models.FloatField(max_length=7, default=15000)
