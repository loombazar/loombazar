from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'home/base.html')

def product_details(request):
    return render(request,'home/product_details.html')

def contact_page(request):
    return render(request,'home/contact.html')

def cart_page(request):
    return render(request,'home/shop-cart.html')

def checkout_page(request):
    return render(request,'home/checkout.html')

def login_page(request):
    return render(request,'home/login.html')