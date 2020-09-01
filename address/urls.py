from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('add_new_address',views.add_new_address,name='add_new_address'),
    path('edit_address',views.edit_address,name='edit_address'),
    path('delete_address',views.delete_address,name='delete_address'),
]