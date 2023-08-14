from django.db import models
from tkinter import CASCADE

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.category_name
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.FloatField()
    image_url=models.FileField(upload_to='static/uploads',null=True)
    product_stock= models.IntegerField()
    product_description = models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_name
    
class Casarsoul(models.Model):
    image_url=models.FileField(upload_to='static/uploads',null=True)
