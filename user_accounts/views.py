from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .models import User

# Create your views here.
def logout(request):
    auth.logout(request)

    return redirect('index')

def test(request):
    pass

def reg_form(request):
    if request.method == 'POST':
        gen_mark = request.POST['gender-mark']
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']

        user = User.objects.create_user(gender_mark=gen_mark,full_name=name,email=email,password=password,mobile_number=mobile)
        user.save()
        return redirect('/')

    else:
        return redirect('login_page')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return redirect('login_page')
    else:
        return redirect('login_page')