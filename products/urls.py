from django.urls import path
from . import views

urlpatterns = [
   path('product_details/<int:pk>/',views.product_details,name='product_details'),
]
