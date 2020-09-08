# Generated by Django 2.2.7 on 2020-09-07 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200906_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
