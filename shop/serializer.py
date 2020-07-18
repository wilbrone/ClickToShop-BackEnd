from rest_framework import serializers
from .models import *

class MerchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'bio', 'phone_number')


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'description', 'price', 'img_url')

    def save(self):
        # request = self.context.get("request")
        pass