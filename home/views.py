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

    full_name = ''
    first_name = ''
    last_name = ''
    user = request.user
    if user.first_name:
        first_name = user.first_name
    if user.last_name:
        last_name = user.last_name

    if user.full_name:
        full_name = user.full_name
    else:
        full_name = first_name + " " + last_name
    dob = user.dob
    gender = user.gender
    mobile = user.mobile_number


    context = {
        'full_name' : full_name,
        'dob' : dob,
        'gender':gender,
        'mobile_number':mobile
    }

    return render(request,'home/user_profile.html',context)

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



