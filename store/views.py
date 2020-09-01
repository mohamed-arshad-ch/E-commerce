from django.shortcuts import render

# Create your views here.
def store(request):
    context = {}
    return render(request,'index.html',context)

def cart(request):
    context = {}
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