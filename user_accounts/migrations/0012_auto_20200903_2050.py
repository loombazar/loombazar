# Generated by Django 2.2.7 on 2020-09-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0011_auto_20200903_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
