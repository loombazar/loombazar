from django import forms
from .models import Address
class address_form(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('pin_code','district','state','full_name','address','landmark','mobile_number')

