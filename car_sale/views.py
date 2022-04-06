from re import search
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CarSaler
from car_sale.models import CarSaler
from .forms import CarSaleForm
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q



def home(request):
    search_text = request.POST.get('search')
    if search_text:
        user_list = CarSaler.objects.filter(Q(year__icontains=search_text) | Q(make__icontains=search_text))
        if user_list:
            page = request.GET.get('page', 1)
            paginator = Paginator(user_list,4)
            try:
                users = paginator.page(page)
            except PageNotAnInteger:
                users = paginator.page(1)
            except EmptyPage:
                users = paginator.page(paginator.num_pages)

            return render(request, 'home.html', { 'users': users })       
        else:
            return render(request, 'not_found.html')        
        
    else:
        
        user_list = CarSaler.objects.all().order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(user_list,4)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

        return render(request, 'home.html', { 'users': users })

   


def car_saler_form(request):
    saler = CarSaleForm()
    if request.method == 'POST':
        saler = CarSaleForm(request.POST, request.FILES)
        if saler.is_valid():
            saler.save()
            return redirect('success')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'home'}}">reload</a>""")
    else:
        return render(request, 'car_saler_form.html', {'upload_form': saler})
    
    
def successform(request):
    id = CarSaler.objects.latest('id').id
    return render(request, 'success.html',{'upload_form': id})