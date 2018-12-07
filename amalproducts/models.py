from django.db import models
from django.contrib.auth.models import User    

class Product(models.Model):
    name = models.CharField(max_length=250)
    product_number = models.IntegerField()
    stock = models.IntegerField()
    price = models.FloatField()
    owner = models.ManyToManyField(User)

    def __str__(self):
        return self.name