from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('product_details',views.product_details,name='product_details'),
    path('contact_page',views.contact_page,name='contact_page'),
    path('cart_page',views.cart_page,name='cart_page'),
    path('checkout_page',views.checkout_page,name='checkout_page'),
    path('login_page',views.login_page,name='login_page'),
]
