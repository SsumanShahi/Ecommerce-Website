from django.contrib import admin
from django.urls import path 
from .views import *

urlpatterns = [
    path('register/',user_register),
    path('accounts/login/',user_login),
    path('logout/',user_logout),
    path('dashboard/',dashboard),
    path('total_order/',showPorders),
    path('total_users/',show_users),
    # path('total_admins/',show_staff),


]