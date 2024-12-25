import json
from contextlib import nullcontext

from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.template.context_processors import request

from .form import customuserform
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def homepage(request):
    products=product.objects.filter(trending=1)
    return render(request,'all/home.html',{'products':products})

def cart_page(request):
    if request.user.is_authenticated:
        carts= cart.objects.filter(user=request.user)
        return render(request, 'all/cart.html',{'cart':carts})

    else:
        return redirect("/")

def favviewpage(request):
    if request.user.is_authenticated:
        fav= favourite.objects.filter(user=request.user)
        return render(request, 'all/fav.html',{'fav':fav})

    else:
        return redirect("/")

def delete_cart(request,cid):
    clear=cart.objects.get(id=cid)
    clear.delete()

    return redirect('cart')
def delete_fav(request,cid):
    clear=favourite.objects.get(id=cid)
    clear.delete()

    return redirect('favviewpage')
def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            # print(request.user.id)
            product_status=product.objects.get(id=product_id)
            if product_status:
                if cart.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status': 'product already in cart'}, status=200)
                else:
                    if product_status.quentity >= product_qty:
                        cart.objects.create(user=request.user,product_id=product_id,product_quentity=product_qty)
                        return JsonResponse({'status': 'cart added to a card'}, status=200)
                    else:
                        return JsonResponse({'status': 'product stock is not available'}, status=200)
        else:
            return JsonResponse({'status': 'login to add cart'}, status=200)

    else:
        return JsonResponse({'status':'Invalid Access'},status=200)

def fav_page(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=data['pid']
            # print(request.user.id)
            product_status=product.objects.get(id=product_id)
            if product_status:
                if favourite.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status': 'product already in favourite'}, status=200)
                else:
                    favourite.objects.create(user=request.user, product_id=product_id)
                    return JsonResponse({'status': 'cart added to a favourite'}, status=200)
        else:
            return JsonResponse({'status': 'product added to favourite'}, status=200)

    else:
        return JsonResponse({'status':'Invalid Access'},status=200)

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request,"logged in successfully")
                return redirect("/")
            else:  # If authentication fails
                messages.error(request, "Invalid username or password")  # Display an error message
                return redirect("/login")

        return render(request,'all/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logout successfully")
        return redirect("/")

def register(request):
    form=customuserform()
    if request.method == 'POST':
        form=customuserform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registeration successfully,you can login now")
            return redirect('login')
    return render(request,'all/register.html',{'form':form})

def collection(request):
    Category = category.objects.filter(status=0)
    return render(request,'all/collection.html',{'category':Category})

def collectionview(request,name):
    if (category.objects.filter(name=name,status=0)):
        products=product.objects.filter(category__name=name)
        return render(request,"all/products/index.html",{'products':products,'category_name':name})
    else:
        messages.warning(request,"no such information fount")
        return redirect('collection')

def product_details(request,cname,pname):
    if (category.objects.filter(name=cname, status=0)):
        if (product.objects.filter(name=pname, status=0)):
            products = product.objects.filter(name=pname, status=0).first()
            return render(request, 'all/product_details.html', {'products': products})
        else:
            messages.error("no such project fount in the bazzar")
            return redirect('collection')
    else:
        messages.error("no such product details fount in the page")
        return redirect('collection')