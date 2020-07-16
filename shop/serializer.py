from rest_framework import serializers
from .models import *

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'bio', 'phone_number')