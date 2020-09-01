from django.shortcuts import render
from products.models import Product
from math import ceil
from address.models import Address

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nslides = (n // 4) + ceil((n/4) - (n // 4))
    print(nslides)
    params = {'no_of_slides':nslides,'range':range(1,nslides),'products':products}
    return render(request,'home/index.html',params)


def contact_page(request):
    return render(request,'home/contact.html')

def cart_page(request):
    return render(request,'home/shop-cart.html')

def checkout_page(request):
    return render(request,'home/checkout.html')

def login_page(request):
    return render(request,'home/login.html')

def profile_page(request):
    return render(request,'home/user_profile.html')

def order_history(request):
    return render(request,'home/order_history.html')

def payment_method(request):
    return render(request,'home/payment_method.html')

def delivary_address(request):
    adds = Address.objects.filter(email=request.user.email).order_by('-date')
    context={
        'adds':adds,
    }
    return render(request,'home/delivary_address.html',context)

def faqs(request):
    return render(request,'home/faqs.html')

def contact_us(request):
    return render(request,'home/contact_us.html')

def legal_information(request):
    return render(request,'home/legal_information.html')

def wishlist(request):
    return render(request,'home/wishlist.html')



