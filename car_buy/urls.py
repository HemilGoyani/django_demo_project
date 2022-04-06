from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.car_buyer, name='car-buyer-form'),
    path('car-buyer-save/<int:id>', views.car_buyer_save, name='car-buyer-save')
]