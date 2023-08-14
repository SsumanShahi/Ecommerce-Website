from django.db import models
from demo_app.models import *
from tkinter import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Order(models.Model):
    Payment=(
        ('Cash on Delivery','Cash on Delivery'),
        ('Esewa','Esewa'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True)
    total_price=models.IntegerField(null=True)
    status=models.CharField(default="PENDING",max_length=200,null=True)
    payment_method=models.CharField(max_length=200,choices=Payment,null=True)
    payment_status=models.BooleanField(max_length=200,default=False,null=True)
    contact_no=models.CharField(max_length=15,null=True)
    address=models.CharField(max_length=50)
    order_date=models.DateTimeField(auto_now_add=True)