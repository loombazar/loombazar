from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('add_new_address',views.add_new_address,name='add_new_address'),
    path('edit_address',views.edit_address,name='edit_address'),
    path('delete_address',views.delete_address,name='delete_address'),
    path('checkout_new_address',views.checkout_new_address,name='checkout_new_address'),
    path('checkout_edit_address',views.checkout_edit_address,name='checkout_edit_address'),
]