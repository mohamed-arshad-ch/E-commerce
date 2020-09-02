from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'index.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0}
    context = {'items':items, 'order':order}
    return render(request,'cart.html',context)

def checkout(request):
    context = {}
    return render(request,'checkout.html',context)

def contact(request):
    context = {}
    return render(request,'contact.html',context)

def shopgrid(request):
    context = {}
    return render(request,'shop-grid.html',context)