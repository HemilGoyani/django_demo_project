from django.urls import path
from . import views


urlpatterns = [
    
    path('car-buyer-form/<int:id>', views.car_buyer, name='car-buyer-form') 
]