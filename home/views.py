from django.shortcuts import render
from products.models import Product
from math import ceil

# Create your views here.
def index(request):
<<<<<<< HEAD
    return render(request,'home/base.html')
=======
    products = Product.objects.all()
    print(products)
    n = len(products)
    nslides = (n // 4) + ceil((n/4) - (n // 4))
    print(nslides)
    params = {'no_of_slides':nslides,'range':range(1,nslides),'products':products}
    return render(request,'home/index.html',params)
>>>>>>> 39a72de21b0eb6a6954c97ce16834b230c59830d


def contact_page(request):
    return render(request,'home/contact.html')

def cart_page(request):
    return render(request,'home/shop-cart.html')

def checkout_page(request):
    return render(request,'home/checkout.html')

def login_page(request):
    return render(request,'home/login.html')