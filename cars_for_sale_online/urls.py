"""cars_for_sale_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from user_authentication.views import loginPage, registerPage, logoutUser
from car_buy.views import car_buyer, car_buyer_save
from car_sale.views import resale
urlpatterns = [
    path('sign-up/', registerPage, name="register"),
    path('login/', loginPage, name="login"),
    path('admin/', admin.site.urls),
    path('', include('car_sale.urls')),
    path('car-buyer-form/<int:id>', car_buyer, name="car-buyer-form"),
    path('car-buyer-savedata/<int:id>',
         car_buyer_save, name="car-buyer-savedata"),
    path('logout/', logoutUser, name="logout"),
    path('resale/<int:id>', resale, name="resale")

]
