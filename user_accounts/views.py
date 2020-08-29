from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .models import User
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from random import sample


# Create your views here.
def logout(request):
    auth.logout(request)

    return redirect('index')

def test(request):
    pass

def reg_form(request):
    if request.method == 'POST':
        gen_mark = request.POST['gender_mark']
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']

        user = User.objects.create_user(gender_mark=gen_mark,full_name=name,email=email,password=password,mobile_number=mobile)
        user.save()
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'Register successfully')
            return redirect('index')

    else:
        return redirect('login_page')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'Login successfully')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Email or Password')
            return redirect('login_page')
    else:
        return redirect('login_page')

def login_page_email(request):
    email = request.GET.get('email',None)
    data = {
        'is_exist': User.objects.filter(email__iexact = email).exists()
    }
    return JsonResponse(data)

def generate_otp():
    list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','a','b','c','x','y','z','0','1','2','3','4','5','6','7','8','9']
    otp = sample(list,4)
    otp_str = ''.join(otp)
    return otp_str

def forget_sent_email(request):
    email = request.GET.get('email',None)
    print(email)
    otp = generate_otp()
    subject = 'LoomBazar Reset Password'
    message = 'Your OTP to reset your password is : ' + str(otp)
    sender = 'loombazar.official@gmail.com'
    send_mail(subject,message,sender,[email],fail_silently=False)
    
    data = {
        'otp': otp
    }
    return JsonResponse(data)

