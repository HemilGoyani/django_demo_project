from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("car-saler-form/", views.car_saler_form, name="car-saler-form"),
    path('success/', views.successform, name='success')
]
