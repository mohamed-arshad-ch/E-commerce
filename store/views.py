from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import *
import json

# Create your views here.

    

def store(request):
    products = Product.objects.all()
    
   
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=customer,complete=False)
        items = order.orderitem_set.all()
       
    else:
        items = []
        order = {'get_cart_total':0}
    context = {'products':products,'items':items, 'order':order}
    return render(request,'index.html',context)
    

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=customer,complete=False)
        items = order.orderitem_set.all()
        print("gvkvvhgvhgvhgvhgvghv")
        
    else:
        items = []
        order = {'get_cart_total':0}
    context = {'items':items, 'order':order}
    return render(request,'cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0}
    context = {'items':items, 'order':order}
    
    return render(request,'checkout.html',context)

def contact(request):
    context = {}
    return render(request,'contact.html',context)

def shopgrid(request):
    context = {}
    return render(request,'shop-grid.html',context)

def productdetails(request,id):
    products = Product.objects.get(id=id)
    context = {'products':products}
    return render(request,'product-details.html',context) 

def updateitem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:',action)
    print('Product:',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(Customer=customer,complete=False)

    orderItem, created = Order.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('it was added',safe=False)
    
