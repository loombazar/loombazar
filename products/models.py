from django.db import models

# Create your models here.
class Product(models.Model):

    people_category_choice = (
        ('Men','Men'),
        ('Women','Women'),
        ('Kids','Kids'),
        ('Home Decor','Home Decor'),
        ('Accessories','Accessories'),
    )

    category_choice = (
        ('Top Wear','Top Wear'),
        ('Bottom Wear','Bottom Wear'),
        ('Fastive Wear','Fastive Wear'),
        ('Indian & Fusion Wear','Indian & Fusion Wear'),
        ('Sarees','Sarees'),
        ('Boys Clothing','Girls Clothing'),
        ('Bed Line','Bed Line'),
        ('Duptta','Duptta'),
        ('Dress Materials','Dress Materials'),
    )

    sub_category_choice = (
        ('T_shirts','T_shirts'),
        ('Casual Shirt','Casual Shirt'),
        ('Formal Shirt','Formal Shirt'),
        ('Jackets','Jackets'),
        ('Blazer & Coats','Blazer & Coats'),
        ('Suits','Suits'),
        ('Casual Trouser','Casual Trouser'),
        ('Formal Trouser','Formal Trouser'),
        ('Shorts','Shorts'),
        ('Track Paints','Track Paints'),
        ('Kurta & Kurtaset','Kurta & Kurtaset'),
        ('Sherwanis','Sherwanis'),
        ('Nehru Jackets','Nehru Jackets'),
        ('Dhoti','Dhoti'),
        ('Badsheet','Badsheet'),
        ('Blanket','Blanket'),
        
    )

    size_choice = (
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('XXL','XXL'),
    )

    product_name = models.CharField(max_length=200,null=False,blank=False)
    product_brand = models.CharField(max_length=100,null=True,blank=True)
    actual_price = models.CharField(max_length=50,null=False,blank=False)
    discount_price = models.CharField(max_length=50,null=True,blank=True)
    discount_percentage = models.CharField(max_length=50,null=True,blank=True)
    people_category = models.CharField(max_length=100,null=True,blank=True,choices=people_category_choice)
    category = models.CharField(max_length=200,null=False,blank=False,choices=category_choice)
    sub_category = models.CharField(max_length=200,null=True,blank=True,choices=sub_category_choice)
    color = models.CharField(max_length=100,blank=True,null=True)
    size = models.CharField(max_length=50,blank=True,null=True,choices=size_choice)
    ratings = models.CharField(max_length=20,null=True,blank=True,default='5.0')
    stock = models.CharField(max_length=30,null=True,blank=True)
    image1 = models.ImageField(upload_to='product_images',null=False,blank=False)
    image2 = models.ImageField(upload_to='product_images',null=True,blank=True)
    image3 = models.ImageField(upload_to='product_images',null=True,blank=True)
    image4 = models.ImageField(upload_to='product_images',null=True,blank=True)

    def __str__(self):
        return self.product_name + " " + self.category
