# Generated by Django 2.1.4 on 2018-12-06 18:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('amalproducts', '0002_remove_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
