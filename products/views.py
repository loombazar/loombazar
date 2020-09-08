from django.shortcuts import render
from .models import Product
# Create your views here.
def product_details(request,pk):
    prod = Product.objects.get(pk=pk)
    products = Product.objects.all()
    params = {'prod':prod}
    

    return render(request,'home/product_details.html',params)

    