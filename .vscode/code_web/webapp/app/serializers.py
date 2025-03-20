from rest_framework import serializers
from .models import Checkout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
import sys
from django.contrib.auth import get_user_model
class CheckOutSerializer(serializers.ModelSerializer):
    valid_product = ['Em meo', 'Em vit hanh', 'Empe']
    class Meta:
        model = Checkout
        fields = ['nameproduct', 'price',]
    def validate_price(self,value):
        if value < 0:
            raise serializers.ValidationError("Giá không hợp lệ")
        return value
    def validate_nameproduct(self,value):
        if value not in self.valid_product:
            raise serializers.ValidationError("Tên sản phẩm không hợp lệ")
        return value
    def create(self, validated_data):
        request = self.context.get('request')# Lấy user từ request
        print(f"tao in ra : {request.user.is_authenticated}")
        if request:  
                user_id = int(request.session.get('_auth_user_id'))
                user_instance = User.objects.get(id=user_id)
                validated_data['id_username'] = user_instance
                print("Validated data after adding user_id:", validated_data)
                validated_data['username'] = user_instance
                print("Validated data after adding user_id:", validated_data)
                print(validated_data) 
                    # Gán object user vào
                # Lấy user từ session  # Gán user vào dữ liệu
        return super().create(validated_data)
    