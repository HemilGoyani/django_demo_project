from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('home/', views.home, name="home"),
    # path('car-buy/', include('car_buy.urls')),
]
