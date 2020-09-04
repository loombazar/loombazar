from django.urls import path
from . import views

urlpatterns = [
   path('logout',views.logout,name='logout'),
   path('reg_form',views.reg_form,name='reg_form'),
   path('login',views.login,name='login'),
   path('login_page_email',views.login_page_email,name='login_page_email'),
   path('forget_sent_email',views.forget_sent_email,name='forget_sent_email'),
   path('reset_password',views.reset_password,name='reset_password'),
   path('edit_profile',views.edit_profile,name='edit_profile'),
   
]
