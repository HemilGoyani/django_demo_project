# Generated by Django 3.2.10 on 2022-04-05 03:36

from django.db import migrations
import djmoney.models.fields
import djmoney.models.validators
import djmoney.money


class Migration(migrations.Migration):

    dependencies = [
        ('car_sale', '0003_rename_carseller_carsaler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsaler',
            name='asking_price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=8, validators=[djmoney.models.validators.MinMoneyValidator(djmoney.money.Money(1000, 'USD')), djmoney.models.validators.MaxMoneyValidator(djmoney.money.Money(100000, 'USD'))]),
        ),
    ]
