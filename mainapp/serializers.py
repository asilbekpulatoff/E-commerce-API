from rest_framework import serializers
from mainapp.models import Category, Product, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity','description', 'price', 'category')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user_profile', 'product', 'quantity', 'location')
    
    def create(self, validated_data):
        obj = Order.objects.create(**validated_data)
        product = Product.objects.get(id=obj.product.id)
        product.quantity -= validated_data['quantity']
        product.save()
        return obj



