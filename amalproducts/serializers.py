from rest_framework import serializers
from amalproducts.models import Product
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class ProductSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'product_number', 'stock', 'price', 'owner')
