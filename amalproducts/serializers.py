from rest_framework import serializers
from amalproducts.models import Product
from django.contrib.auth.models import User

# class UserProductSerializer(serializers.ModelSerializer):
#     id = serializers.ReadOnlyField(source='member.id')
#     name = serializers.ReadOnlyField(source='member.name')

#     class Meta:
#         model = UserProduct
#         fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=250)
    product_number = serializers.IntegerField()
    stock = serializers.IntegerField()
    price = serializers.FloatField()
    owner = UserSerializer(many=True)
