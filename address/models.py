from django.db import models
from user_accounts.models import User
# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    pin_code = models.CharField(max_length=30,null=False,blank=False)
    district = models.CharField(max_length=100,null=False,blank=False)
    state = models.CharField(max_length=100,blank=False,null=False)
    full_name = models.CharField(max_length=200,null=False,blank=False)
    address = models.CharField(max_length=250,null=False,blank=False)
    landmark = models.CharField(max_length=200,blank=True,null=True)
    mobile_number = models.CharField(max_length=15,null=False,blank=False)
    email = models.EmailField(null=True,blank=True)

    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name

    def update_address(self,pin_code,district,state,full_name,address,landmark,mobile_number):
        
        self.pin_code = pin_code
        self.district = district
        self.state = state
        self.full_name = full_name
        self.address = address
        self.landmark = landmark
        self.mobile_number = mobile_number
        self.save()