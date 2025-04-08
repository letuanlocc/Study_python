from rest_framework import serializers
from .models import Checkout
from .models import Warehouse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
import sys
from django.contrib.auth import get_user_model
class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ['id_product','id_username','nameproduct', 'price', 'quantity', 'date_time']
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['nameproduct','origin','price','instock','image']
        
    def update(self, instance, validated_data):
        image = validated_data.get('image', None) 
        if image is None:  # Nếu không có ảnh mới, giữ ảnh cũ
            validated_data['image'] = instance.image
        return super().update(instance, validated_data)