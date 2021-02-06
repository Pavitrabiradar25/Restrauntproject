"""Restrauntproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from restrauntapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',views.home_page_view),
    path('food_category/',views.food_category),
    path('food_item/',views.food_item),
    path('gujrat/',views.gujrat_food),
    path('panjabi/',views.panjab_food),
    path('tamil/',views.tamil_food),
    path('bengali/',views.bengali_food),
    path('rajastani/',views.rajastani_food),
    path('maharashtra/',views.maharashtra_food),
    path('kar/',views.kar_food),
    path('kerala/',views.kerala_food),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/',views.logout_page), 
    path('signup/',views.signup_page),
    path('welcome/',views.welcome_user),
    path('search/',views.search),
    path('result/',views.result),
]
