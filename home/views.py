from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'home/index.html')

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
def profile_page(request):
    return render(request,'home/user_profile.html')
def order_history(request):
    return render(request,'home/order_history.html')
def payment_method(request):
    return render(request,'home/payment_method.html')
def delivary_address(request):
    return render(request,'home/delivary_address.html')
def faqs(request):
    return render(request,'home/faqs.html')
def contact_us(request):
    return render(request,'home/contact_us.html')
def legal_information(request):
    return render(request,'home/legal_information.html')
def wishlist(request):
    return render(request,'home/wishlist.html')



