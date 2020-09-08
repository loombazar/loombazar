from django.contrib import admin
from .models import Product,Colors,Sizes
# Register your models here.
admin.site.register(Product)
admin.site.register(Colors)
admin.site.register(Sizes)