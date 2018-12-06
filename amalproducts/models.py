from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    product_number = models.IntegerField()
    stock = models.IntegerField()
    price = models.FloatField()

    class Meta:
        ordering = ('product_number',)