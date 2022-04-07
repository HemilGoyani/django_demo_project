
from django.http import HttpResponse
from django.shortcuts import render
from cars_for_sale_online.settings import EMAIL_HOST_USER
from .forms import *
from car_sale.models import CarSaler
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string


def car_buyer(request, id):
    car_id = int(id)
    car_data = CarSaler.objects.get(id=car_id)
    return render(request, 'car_buyer_form.html', {'data': car_data})


def car_buyer_save(request, id):
    car_id = int(id)

    if request.method == 'POST':
        buyer_save = CarBuyerForm(request.POST, request.FILES)
        
        if buyer_save.is_valid():

            name = request.POST.get('buyer_name')
            number = request.POST.get('buyer_mobile')
            email = request.POST.get('email')
            make = request.POST.get('make')
            model = request.POST.get('model')
            year = request.POST.get('year')
            condition = request.POST.get('condition')
            # asking_price = request.POST.get('asking_price')

            buyer_data = CarBuyer(buyer_name=name, buyer_mobile=number, email=email, make=make,
                                  model=model, year=year, condition=condition)
            buyer_data.save()
            car_sold = CarSaler.objects.get(id=car_id)
            
            car_sold.is_sell = True
            car_sold.save()
            print(car_sold.saler_name)
            msg_html = render_to_string('email.html', {'client': car_sold})
            subject = 'Car buyer data'
            message = 'Hope you are enjoying your Django Tutorials'
            recepient = 'hemil.tagline@gmail.com'

            send_mail(subject,
                      message, EMAIL_HOST_USER, [recepient], html_message=msg_html, fail_silently=False)
            return render(request, 'regsuccess.html')

        else:
            return HttpResponse('Form is not valid, please validate the form')
