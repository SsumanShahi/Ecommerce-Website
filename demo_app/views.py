from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from accounts.auth import *

# Create your views here.
def demo(request):
    return HttpResponse("Hi from demo app")

@admin_only
def post_product(request):
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Product Added")
            return redirect("/product/addproduct")
        else:
            messages.add_message(request,messages.ERROR,"Product not added")
            return render(request,'demo/addproduct.html',{
                'form': ProductForm
            })
    context={
        'form': ProductForm
        }
    return render(request,'demo/addproduct.html',context)

@admin_only
def show_product(request):
    products = Product.objects.all()
    context ={
        'products':products
    }
    return render(request, 'demo/index.html',context)

def sample(request):
    return render(request,'demo/sample.html')

@admin_only
def post_category(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Category Added")
            return redirect("/product/addcategory")
        else:
            messages.add_message(request,messages.ERROR,"Category not added")
            return render(request,'demo/addcategory.html',{
                'form': CategoryForm
            })
    context={
        'form': CategoryForm
    }
    return render(request,'demo/addcategory.html',context)

@admin_only
def show_category(request):
    categories=Category.objects.all()
    context={
        'category':categories
    }
    return render(request,'demo/showcategory.html',context)

@admin_only
def delete_product(request,product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    return redirect('/product/showproduct')

@admin_only
def update_product(request,product_id):
    product=Product.objects.get(id=product_id)
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Product updated")
            return redirect("/product/showproduct")
        else:
            messages.add_message(request,messages.ERROR,"Product not updated")
            return render(request,'demo/updateproduct.html',{
                'form': ProductForm(instance=product)
            })
    context={
        'form':ProductForm(instance=product)
    }
    return render(request,'demo/updateproduct.html',context)

@admin_only
def update_category(request,category_id):
    category=Category.objects.get(id=category_id)
    if request.method=="POST":
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Category Updated")
            return redirect("/product/showcategory")
        else:
            messages.add_message(request,messages.ERROR,"Category Not Updated")
            return render(request,'demo/updatecategory.html',{
                'form':CategoryForm(instance=category)
            })
    context={
        'form':CategoryForm(instance=category)
    }
    return render(request,'demo/updatecategory.html',context)

@admin_only
def delete_category(request,category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    return redirect('/product/showcategory')

@admin_only
def post_carasoul(request):
    if request.method=="POST":
        form=CasarsoulForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"image added")
            return redirect("/product/addcarasoul")
        else:
            messages.add_message(request,messages.ERROR,"image not added ")
            return render(request,'demo/addcarasoul.html',{
                'carasoul':CasarsoulForm
            })
    context={
            'carasoul':CasarsoulForm
        }
    return render(request,'demo/addcarasoul.html',context)






