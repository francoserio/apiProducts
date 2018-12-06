from rest_framework import serializers
from amalproducts.models import Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=250)
    product_number = serializers.IntegerField()
    stock = serializers.IntegerField()
    price = serializers.FloatField()
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        return Product.objects.create(**validated_data, owner=self.request.user)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.price = validated_data.get('price', instance.price)
        instance.product_number = validated_data.get('product_number', instance.product_number)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save(owner=self.request.user)
        return instance