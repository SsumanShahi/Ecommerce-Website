from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from .auth import *
from users.models import *

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid(): #yesma vako "form" xuttai 
            form.save()
            messages.add_message(request,messages.SUCCESS,'User Created Successfully')
            return redirect('/register')
        else:
            context={
                'form':UserCreationForm #yesma vako 'form' xuttai ho mathi ma vako form xuttai ho
            }
            return render(request,'account/register.html',context)
    context={
        'form':UserCreationForm
    }
    return render(request, 'account/register.html',context)

def user_login(request):
    if request.method=="POST":
        form=Loginform(request.POST)
        if form.is_valid():
            form=form.cleaned_data
            user=authenticate(request,username=form['username'],password=form['password'])
            if user is not None:
                login(request,user)
                return redirect('/dashboard')
            else:
                messages.add_message(request,messages.ERROR,"Login Failed")
                context={
                    'form':Loginform
                }
                return render(request,'account/login.html',context)
    context={
        'form':Loginform
    }
    return render(request,'account/login.html',context)

def user_logout(request):
    logout(request)
    return redirect("/accounts/login")


@login_required
@admin_only

def dashboard(request):
    return render(request,'account/dashboard.html')

def showPorders(request):
    t_orders=Order.objects.all()
    context={
        'order':t_orders
    }
    return render(request,'account/total_order.html',context)

def show_users(request):
    s_users=User.objects.all()
    context={
        'users':s_users
    }
    return render(request,'account/show_users.html',context)

# def show_staff(request):
    
#     s_staff=User.objects.filter(User.is_staff==1)
#     context={
#         'staff':s_staff
#     }
#     return render(request,"account/show_admins.html",context)
    