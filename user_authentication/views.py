from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import CreateUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect 

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from car_sale.models import CarSaler
from car_sale.views import home

def registerPage(request):  
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
        

    context = {'form':form}
    return render(request, 'register.html', context)


def loginPage(request):
	
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('home')


    