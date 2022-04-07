from re import search
from django.http import HttpResponse
from django.shortcuts import render, redirect

from car_buy.models import CarBuyer
from .models import CarSaler
from car_sale.models import CarSaler
from .forms import CarSaleForm
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def home(request):
    search_text = request.POST.get('txtsearch')
    if search_text:
        user_list = CarSaler.objects.filter(
            Q(year__icontains=search_text) | Q(make__icontains=search_text))

        if user_list:
            paginator = Paginator(user_list, 4)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, 'home.html', {'users': page_obj, 'searchval': search_text})
        else:
            return render(request, 'not_found.html')

    else:

        user_list = CarSaler.objects.all().order_by('-id')
        paginator = Paginator(user_list, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'home.html', {'users': page_obj})


def car_saler_form(request):
    saler = CarSaleForm()
    if request.method == 'POST':
        saler = CarSaleForm(request.POST, request.FILES)
        if saler.is_valid():
            saler.save()
            return redirect('success')
        else:
            return render(request, "car_saler_form.html", {'upload_form': saler})

    else:
        return render(request, 'car_saler_form.html', {'upload_form': saler})


def successform(request):
    id = CarSaler.objects.latest('id').id
    return render(request, 'success.html', {'upload_form': id})


def resale(request, id):
    car_id = int(id)
    resale = CarSaler.objects.get(id=car_id)
    resale.is_sell = False
    resale.save()

    return render(request, 'available.html')
