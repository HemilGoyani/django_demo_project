from django.http import HttpResponse
from django.shortcuts import render, redirect

from car_sale.models import CarSaler
from .forms import CarSaleForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def car_saler_form(request):
    saler = CarSaleForm()
    if request.method == 'POST':
        saler = CarSaleForm(request.POST, request.FILES)
        if saler.is_valid():
            
            saler.save()
            # id = CarSaler.objects.latest('id').id
            return redirect('success')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'home'}}">reload</a>""")
    else:
        return render(request, 'car_saler_form.html', {'upload_form': saler})

def successform(request):
    id = CarSaler.objects.latest('id').id
    print(id,"=-=-=")
    return render(request, 'success.html',{'upload_form': id})