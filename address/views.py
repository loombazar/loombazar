from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Address
from user_accounts.models import User
from .forms import address_form
# Create your views here.
def add_new_address(request):
    if request.method == 'POST':
        pin_code = request.POST['pin_code']
        district = request.POST['district']
        state = request.POST['state']
        full_name = request.POST['full_name']
        address = request.POST['address']
        landmark = request.POST['landmark']
        mobile_number = request.POST['mobile_number']

        addr = Address.objects.create(email=request.user.email,pin_code = pin_code,district=district,state=state,full_name=full_name,address=address,landmark=landmark,mobile_number=mobile_number)
        addr.save()

        adds = Address.objects.filter(email=request.user.email)
        print(adds)
        context ={
            'adds':adds
        }
        return render(request,'home/delivary_address.html',context)
    else:
        return render(request,'home/delivary_address.html',context)


def delete_address(request):
    pk = request.POST['del_address_pk']
    print(pk)
    addr = Address.objects.get(pk=pk)
    addr.delete()
    return redirect('delivary_address')

def edit_address(request):
    pk = request.POST['edit_address_pk']
    addr = Address.objects.get(pk=pk)
    full_name = request.POST['full_name']
    address = request.POST['address']
    landmark = request.POST['landmark']
    district = request.POST['district']
    state = request.POST['state']
    pin_code = request.POST['pin_code']
    mobile = request.POST['mobile_number']
    
    addr.update_address(full_name=full_name,address=address,landmark=landmark,district=district,state=state,pin_code=pin_code,mobile_number=mobile)
    return redirect('delivary_address')
