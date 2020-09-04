from django.shortcuts import render
from products.models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nslides = (n // 4) + ceil((n/4) - (n // 4))
    print(nslides)
    params = {'no_of_slides':nslides,'range':range(1,nslides),'products':products}
    return render(request,'home/index.html',params)





