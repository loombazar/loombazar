from django.urls import path
from . import views

urlpatterns = [
   path('logout',views.logout,name='logout'),
   path('reg_form',views.reg_form,name='reg_form'),
   path('login',views.login,name='login'),
   path('login_page_email',views.login_page_email,name='login_page_email'),
]
