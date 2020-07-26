from rest_framework import serializers
from .models import *


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'phone_number')

            
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'description', 'price', 'img_url')

    def save(self):
        pass
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product','quantity','t_price')

    # def save(self):
    #     # request = self.context.get("request")
    #     pass