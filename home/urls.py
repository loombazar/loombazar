from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    
    path('contact_page',views.contact_page,name='contact_page'),
    path('cart_page',views.cart_page,name='cart_page'),
    path('checkout_page',views.checkout_page,name='checkout_page'),
    path('login_page',views.login_page,name='login_page'),
    path('profile_page',views.profile_page,name='profile_page'),
    path('order_history',views.order_history,name='order_history'),
    path('payment_method',views.payment_method,name='payment_method'),
    path('delivary_address',views.delivary_address,name='delivary_address'),
    path('faqs',views.faqs,name='faqs'),
   
    path('contact_us',views.contact_us,name='contact_us'),
    path('legal_information',views.legal_information,name='legal_information'),
    path('wishlist',views.wishlist,name='wishlist'),

]
