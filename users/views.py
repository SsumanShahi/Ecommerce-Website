from django.shortcuts import render,redirect
from demo_app.models import *
from django.contrib.auth.decorators import login_required
from accounts.auth import *
from users.models import *
from django.contrib import messages
from .forms import *
from demo_app.models import *

# Create your views here.
def homepage(request):
    product=Product.objects.all().order_by('-id')[:8]
    context={
        'form':product
    }
    return render(request,"users/homepage.html",context)

def productdetail(request, product_id):
    productdetail = Product.objects.get(id=product_id)
    context={
        'product':productdetail
    }
    return render(request,'users/productdetail.html',context)

def product(request):
    product= Product.objects.all()
    context={
        'form':product
    }
    return render(request,'users/products.html',context)


@login_required
@user_only
def add_to_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    user=request.user
    check_item=Cart.objects.filter(product=product,user=user)
    if check_item:
        messages.add_message(request,messages.ERROR,"Product already in cart")
        return redirect('/mycart')
    else:
        cart=Cart.objects.create(user=user,product=product)
        if cart:
            messages.add_message(request,messages.SUCCESS,"Product added sucessfully")
            return redirect('/mycart')
        else:
            messages.add_message(request,messages.ERROR,"Product not added sucessfully")
            return redirect('/products')
        
@login_required
@user_only
def show_cart_item(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    context={
        'cart':cart
    }
    return render(request,'users/mycart.html',context)

def delete_cart_item(request,cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    messages.add_message(request,messages.SUCCESS,"item remove from cart")
    return redirect("/mycart")

def order(request,product_id,cart_id):
    product=Product.objects.get(id=product_id)
    cart=Cart.objects.get(id=cart_id)
    user=request.user
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            quantity=request.POST.get('quantity')
            price=product.product_price
            total_price=int(quantity)*int(price)
            contact_no=request.POST.get("contact_no")
            address=request.POST.get("address")
            payment_method=request.POST.get("payment_method")
            payment_status=request.POST.get("payment_status")
            status=request.POST.get('status')

            order=Order.objects.create(
                product=product,
                user=user,
                quantity=quantity,
                total_price=total_price,
                contact_no=contact_no,
                address=address,
                payment_method=payment_method,
                payment_status=payment_status,
                status=status
            )
            if order.payment_method=="Cash on Delivery":
                cart=Cart.objects.get(id=cart_id)
                cart.delete()
                messages.add_message(request,messages.SUCCESS,"order successful")
                return redirect("/mycart")
            elif(order.payment_method=="Esewa"):
                context={
                    'order':order,
                    'cart':cart,
                }
                return render(request,"users/esewa_payment.html",context)
            else:
                messages.add_message(request,messages.ERROR,"Something went wrong")
                return render(request,"users/order_page.html",{
                    'form':OrderForm
                })

    context={
        'form':OrderForm
    }
    return render(request,'users/order_page.html',context)

@login_required
def user_order(request):
    user=request.user
    order=Order.objects.filter(user=user)
    context={
        'order':order
    }
    return render(request,"users/userorder.html",context)

@login_required
@admin_only
def admin_order(request):
    order=Order.objects.all()
    context={
        'order':order
    }
    return render(request,'users/adminorder.html',context)

def esewa_verify(request):
    import xml.etree.ElementTree as ET
    o_id= request.GET.get('old')
    amount = request.GET.get('amt')
    refId=request.GET.get('redID')
    url ="https://uat.esewa.com.np/epay/transrec"
    d = {
    'amt': 100,
    'scd': 'EPAYTEST',
    'rid': '000AE01',
    'pid':'ee2c3ca1-696b-4cc5-a6be-2c40d929d453',
}
    resp = request.post(url, d)

def carasoul(request):
    carasoul=Casarsoul.objects.all()
    context={
        'carasoul':carasoul
    }
    return render(request,"users/homepage.html",context)    