# Generated by Django 3.0.3 on 2020-08-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('actual_price', models.CharField(max_length=50)),
                ('discount_price', models.CharField(blank=True, max_length=50, null=True)),
                ('discount_percentage', models.CharField(blank=True, max_length=50, null=True)),
                ('people_category', models.CharField(blank=True, choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids'), ('Home Decor', 'Home Decor'), ('Accessories', 'Accessories')], max_length=100, null=True)),
                ('category', models.CharField(choices=[('Top Wear', 'Top Wear'), ('Bottom Wear', 'Bottom Wear'), ('Fastive Wear', 'Fastive Wear'), ('Indian & Fusion Wear', 'Indian & Fusion Wear'), ('Sarees', 'Sarees'), ('Boys Clothing', 'Girls Clothing'), ('Bed Line', 'Bed Line'), ('Duptta', 'Duptta'), ('Dress Materials', 'Dress Materials')], max_length=200)),
                ('sub_category', models.CharField(blank=True, choices=[('T_shirts', 'T_shirts'), ('Casual Shirt', 'Casual Shirt'), ('Formal Shirt', 'Formal Shirt'), ('Jackets', 'Jackets'), ('Blazer & Coats', 'Blazer & Coats'), ('Suits', 'Suits'), ('Casual Trouser', 'Casual Trouser'), ('Formal Trouser', 'Formal Trouser'), ('Shorts', 'Shorts'), ('Track Paints', 'Track Paints'), ('Kurta & Kurtaset', 'Kurta & Kurtaset'), ('Sherwanis', 'Sherwanis'), ('Nehru Jackets', 'Nehru Jackets'), ('Dhoti', 'Dhoti'), ('Badsheet', 'Badsheet'), ('Blanket', 'Blanket')], max_length=200, null=True)),
                ('color', models.CharField(blank=True, choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=50, null=True)),
                ('ratings', models.CharField(blank=True, default='5.0', max_length=20, null=True)),
                ('stock', models.CharField(blank=True, max_length=30, null=True)),
                ('image1', models.ImageField(upload_to='product_images')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='product_images')),
            ],
        ),
    ]