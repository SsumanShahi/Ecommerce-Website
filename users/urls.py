from django.contrib import admin
from django.urls import path 
from .views import *

urlpatterns = [
    path('',homepage),
    path('productdetail/<int:product_id>/',productdetail),
    path('products/',product),
    path("cart/<int:product_id>",add_to_cart),
    path('mycart/',show_cart_item),
    path('delete_cart/<int:cart_id>',delete_cart_item),
    path('order/<int:product_id>/<int:cart_id>',order),
    path('userorder/',user_order),
    path('adminorder/',admin_order)
]